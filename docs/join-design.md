# データ結合設計書（名寄せ設計）

最終更新: 2026-03-12

---

## 前提

- 全データのCRSは **EPSG:4326 (WGS84)** に統一する
- 距離計算時は **EPSG:2263 (NAD83 / New York Long Island, feet)** に投影するか、簡易メートル変換を使用する
- 簡易変換: `y = lat × 111,320`, `x = lon × 111,320 × cos(40.75°)`。マンハッタン程度の範囲なら誤差 <0.5%

---

## 結合1: OSM Starbucks → MapPLUTO区画

| 項目 | 内容 |
|---|---|
| 左テーブル | OSM Starbucks (171店, EPSG:4326) |
| 右テーブル | PLUTO Manhattan (42,600区画, lat/lon) |
| 結合キー | 座標（nearest join） |
| 結合方法 | `scipy.spatial.cKDTree` による最近隣探索 |
| CRS | 両方EPSG:4326 → メートル変換して距離計算 |
| 閾値 | 100m以内を採用。50m以内で95.9%、100m以内で100%マッチ |
| 想定マッチ率 | **100% (171/171)** |
| 想定欠損率 | **0%** |
| 出力カラム | bbl, landuse, bldgclass, numfloors, yearbuilt, assesstot, retailarea, comarea, lotarea, zonedist1 |

### 設計判断

- **Shapefile（ポリゴン）不要**。PLUTOのポイント座標(centroid)でnearest joinが十分機能する
- 中央値21m、最大72mなので100m閾値でも過剰マッチのリスクなし
- `gpd.sjoin`によるpoint-in-polygon joinは不要（ポリゴンデータの取得が困難なため）
- バッファ付きjoinへの切り替えも不要
- 結合後にサニティチェック: `landuse`が4(Mixed Res/Com)または5(Commercial)であることを確認（84.8%が該当）

---

## 結合2: OSM Starbucks → MTA最寄り駅

| 項目 | 内容 |
|---|---|
| 左テーブル | OSM Starbucks (171店) |
| 右テーブル | MTA Manhattan Stations (161駅) |
| 結合キー | 座標（nearest join） |
| 結合方法 | Phase 1: `cKDTree`直線距離 / Phase 2: `osmnx`ネットワーク距離 |
| 閾値 | 直線500m（96.5%カバー）/ ネットワーク650m推定 |
| 想定マッチ率 | **96.5% (165/171)** — 直線500m以内 |
| 想定欠損率 | **3.5% (6店)** — 全て750m以内なのでネットワーク距離では1km未満 |
| 出力カラム | station_complex_id, station_complex, 直線距離(m), ネットワーク距離(m) |

### 設計判断: 直線距離 vs ネットワーク距離

| 方法 | メリット | デメリット |
|---|---|---|
| 直線距離 (cKDTree) | 高速、実装簡単 | 実際の歩行距離と乖離。マンハッタンでは×1.2-1.4 |
| ネットワーク距離 (OSMnx) | 歩行者視点で正確 | 計算コスト高（171×161≒27,531ペア） |

**推奨**: Phase 1では直線距離で全店舗に最寄り駅を紐付け。Phase 2（分析フェーズ）でOSMnxによるネットワーク距離を計算し、直線距離との比を検証する。

マンハッタンのグリッド構造では直線距離とネットワーク距離の比は概ね1.2-1.4倍。分析上の「最寄り駅」が変わるケースは少ないと予想されるが、交差点の位置やブロックの形状で逆転する可能性がある（特にLower Manhattanの不規則な道路網）。

---

## 結合3: OSM Starbucks → Census Tract (ACS)

| 項目 | 内容 |
|---|---|
| 左テーブル | OSM Starbucks (171店) |
| 右テーブル | TIGER/Line Census Tract ポリゴン (マンハッタン County FIPS=36061) |
| 結合キー | 空間結合 (point-in-polygon) |
| 結合方法 | `gpd.sjoin(how='left', predicate='within')` |
| CRS | TIGER/Line: EPSG:4269 → EPSG:4326に変換後sjoin |
| 想定マッチ率 | **~100%** — Census Tractはマンハッタン全域を隙間なくカバー |
| 想定欠損率 | **~0%** — 水域上の店舗がなければ0% |
| 出力カラム | GEOID (Census Tract ID), TRACTCE |
| ACS結合 | GEOIDをキーにACS 5-Year テーブルをjoin |

### ACSで取得するテーブル

| ACSテーブル | 変数 | 用途 |
|---|---|---|
| B01003 | Total Population | 人口密度 |
| B19013 | Median Household Income | 所得水準 |
| B08301 | Means of Transportation to Work | 通勤手段（徒歩比率） |
| B25001 | Housing Units | 住戸密度 |

### 設計判断

- TIGER/Lineはポリゴンデータなので、ここだけは`gpd.sjoin`のpoint-in-polygonが必要
- Shapefileは軽量（マンハッタンのみ数百KB）なのでダウンロードに問題なし
- ACSデータはCensus APIまたはcensusdata パッケージで取得

---

## 結合4: MTA駅 → Census Tract

| 項目 | 内容 |
|---|---|
| 左テーブル | MTA Manhattan Stations (161駅) |
| 右テーブル | TIGER/Line Census Tract |
| 結合方法 | `gpd.sjoin` point-in-polygon |
| 用途 | 駅周辺の人口・所得情報を紐付け |

---

## 結合5: OSM Starbucks → 競合カフェ (nearest neighbor)

| 項目 | 内容 |
|---|---|
| 左テーブル | OSM Starbucks (171店) |
| 右テーブル | OSM Cafes (1,220件) + Dunkin' (115店) |
| 結合方法 | `cKDTree` で各スタバから半径500m以内の競合カフェ数をカウント |
| 出力カラム | n_competitors_500m, nearest_competitor_dist, nearest_starbucks_dist |
| 用途 | 競合密度・カニバリゼーション（自社店舗間競合）の推定 |

---

## 結合6: OSM Starbucks → 人流データ (MTA乗降数)

| 項目 | 内容 |
|---|---|
| 左テーブル | OSM Starbucks + 最寄りMTA駅 (結合2の結果) |
| 右テーブル | MTA Subway Hourly Ridership |
| 結合キー | `station_complex_id` |
| 結合方法 | pandas merge |
| 集計 | 時間帯別・曜日別の平均乗降数を計算後にjoin |
| 出力カラム | ridership_weekday_am, ridership_weekday_pm, ridership_weekend 等 |

---

## CRS統一ルール

| データソース | 元CRS | 変換先 | 備考 |
|---|---|---|---|
| OSM (Overpass) | EPSG:4326 | そのまま | 基準CRS |
| PLUTO (API) | WGS84 lat/lon | EPSG:4326 | 変換不要 |
| MTA (API) | WGS84 lat/lon | EPSG:4326 | 変換不要 |
| TIGER/Line | EPSG:4269 (NAD83) | EPSG:4326 | `to_crs(4326)` |
| 距離計算用 | EPSG:4326 | EPSG:2263 or 簡易変換 | CRSコメント必須 |

---

## 結合順序（推奨パイプライン）

```
OSM Starbucks (171店)
  ├── × PLUTO nearest join → ビル属性付与 [結合1]
  ├── × MTA nearest join → 最寄り駅付与 [結合2]
  │     └── × MTA Ridership merge → 乗降数付与 [結合6]
  ├── × TIGER/Line sjoin → Census Tract付与 [結合3]
  │     └── × ACS merge → 人口・所得付与
  └── × Cafes/Dunkin' KDTree → 競合密度付与 [結合5]

最終出力: stores_enriched.csv (171行 × ~30カラム)
```
