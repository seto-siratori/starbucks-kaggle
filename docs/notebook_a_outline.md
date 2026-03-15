# Notebook A 構成設計

作成日: 2026-03-13

---

## 設計原則

- **15-25分で読める集客装置**
- 5秒で殴る図が冒頭にある
- コピペで動く汎用テンプレート（OSM + PLUTO + MTA + Census）
- 「スタバはケーススタディ、本質は空間分析の技術」
- Notebook Bへの明確な導線

---

## タイトル案

1. **"Starbucks Dominant Strategy: Spatial Autocorrelation & Competitor Density in Manhattan"**
   - Moran's I, spatial autocorrelation が検索キーワードに入る
2. **"171 Starbucks, 1200 Competitors: Spatial Clustering Analysis with PySAL & OSMnx"**
   - 具体的な数字 + ツール名 → 技術系ユーザーの検索に刺さる
3. **"Why Starbucks Ignores Income (r=0.03) and Chases Foot Traffic (r=0.58)"**
   - 反直感的なフックがタイトルに入る。クリック率は高いが学術的に見えない
4. **"Spatial Analysis of 171 Starbucks Locations: Moran's I, Ripley's K & MTA Ridership"**
   - 手法名を羅列。教科書的だがSEO的に強い
5. **"Manhattan Starbucks: A Spatial Data Science Case Study with OSM, Census & MTA Data"**
   - 「ケーススタディ」を明示。データソース名が検索に引っかかる

### 決定

> **"171 Starbucks vs 1,200 Competitors: Moran's I, Ripley's K & Spatial Clustering in Manhattan (Reusable Template)"**

理由:
- 具体数字（171, 1200）でスケール感を伝える
- **手法名（Moran's I, Ripley's K）を明記** → Kaggleユーザーが検索で打つのは手法名であってビジネス用語ではない
- **"Reusable Template"** → 「読者の再現にかかる時間を極限まで減らす」の看板。コピペで自分の分析に転用できることを約束
- 「Dominant Strategy」は分析者の結論であって検索キーワードではないため削除

---

## 冒頭のフック（5秒で殴る図）

**scatter_map: サイズ=駅乗降客数、色=500m圏内競合数**

このマップ1枚で見える事実:
- 大きい円（乗降客が多い駅の近く）に赤い色（競合が多い）が集中
- 「乗降客数と競合密度の相関 r=0.58」をキャプションに

続けて1文で殴る:
> *"Starbucks locations correlate with subway ridership (r=0.58) but NOT with household income (r=0.03). They don't chase rich neighborhoods — they chase foot traffic."*

---

## セクション構成

### Section 0: Setup & Data Loading (3 cells)
- pip install + imports
- pathlib auto-detect (Kaggle/local)
- CSV読み込み + shape確認

**使うデータ**: stores_enriched_v3.csv（Kaggle Datasetに同梱）

---

### Section 1: The Hook — What Drives Starbucks Location? (3 cells)

**図1**: scatter_map（サイズ=乗降客数、色=競合密度）

**図2**: 2パネル散布図
- 左: 乗降客数 vs 競合密度（r=0.58, 正の相関）
- 右: 世帯年収 vs 競合密度（r=0.03, 無相関）

**書く結論**: 立地選択は所得ではなく人流に依存。「金持ちの街に出す」は神話。

---

### Section 2: How Clustered Are They? — Global Moran's I (3 cells)

**分析**: Census Tract単位のスタバ店舗数でMoran's Iを計算

**図3**: Moran scatterplot（空間ラグ vs 観測値）

**数字**:
- Moran's I = 0.359, p < 0.001, z = 11.26
- 「スタバの配置は空間的にランダムではなく、統計的に有意にクラスター化している」

**汎用テンプレートとしての価値**: `libpysal` + `esda` のMoran's I計算は10行で書ける。読者が自分の都市・自分の業種で再現可能。

---

### Section 3: Where Are the Hotspots? — LISA Cluster Map (3 cells)

**図4**: LISA choropleth map（HH=赤, LL=青, HL=橙, LH=水色）

**数字**:
- High-High (ホットスポット): 30 tracts → Chelsea/Murray Hill に77%集中
- Low-Low (コールドスポット): 5 tracts → Upper Manhattan
- Low-High（周囲は密集だが自分は空白）: 9 tracts → **出店余地の候補**

**書く結論**: ドミナント戦略はマンハッタン全域ではなく、Chelsea〜Midtown の南北2km帯に集中。

---

### Section 4: Tighter Than the Competition — Nearest Neighbor & Ripley's K (4 cells)

**図5**: 最近接距離ヒストグラム（Starbucks vs Dunkin' の重ね合わせ）

**数字**:
- スタバ同士の中央値: 208m
- Dunkin'同士の中央値: 294m
- 比率: 1.41x → **スタバはDunkin'より1.4倍密に自社を配置**

**図6**: Besag's L関数（Starbucks vs Dunkin' + CSR envelope）

**書く結論**: 全距離帯でCSRを超過。スタバのクラスタリングはDunkin'より一貫して強い。これがドミナント戦略の点過程レベルの証拠。

---

### Section 5: Rush Hour Reveals Store Strategy — MTA Hourly Clustering (4 cells)

**図7**: 4クラスターの時間帯別乗降プロファイル折れ線グラフ

**図8**: クラスター別のビル属性クロス集計テーブル

| Cluster | RetailArea | NumFloors | Competitors | Starbucks間隔 |
|---|---|---|---|---|
| Office District | 10,000 sqft | 20F | 44 | 184m |
| Tourism/Shopping | 7,290 | 14F | 38 | 210m |
| Transit Hub | 7,500 | 18F | 36 | 201m |
| Residential | 4,965 | 10F | 13 | 462m |

**書く結論**: Office Districtではスタバが184m間隔で高密度展開（テイクアウト需要）。Residentialは462mと2.5倍の間隔 → 供給不足 or 需要不足の境界線。

---

### Section 6: Limitations & What's Next (2 cells)

**制約の明記**:
- OSMカバレッジ: 85.5%（公式店舗数 ~200 に対し 171）
- 実売上データなし: 駅乗降客数・ビル属性からの推定
- Census Tract粒度: 店舗レベルの需要推定には粗い
- 時間断面: 2024年Q4のスナップショット。出退店の動態は未分析
- 因果関係ではなく相関: 「乗降客数が多いから出店した」のか「出店したから乗降客が増えた」のかは不明

**Notebook Bへの導線**:
> *"This notebook showed WHERE Starbucks clusters. Notebook B asks WHY — building a location scoring model that predicts which Census Tracts are over-served vs under-served."*

**Notebook B で扱う予告**:
- 立地適応度スコアリング（需要代理変数 vs 供給密度）
- 出店候補地ランキングとバックテスト
- OSMnxネットワーク距離による歩行圏分析

---

## Notebook A → Notebook B の仕分け

### Notebook A に入れるもの（記述的分析）
- [x] scatter_map（フック）
- [x] 乗降客数 vs 所得の相関比較
- [x] Global Moran's I
- [x] LISA cluster map
- [x] 最近接距離分布 + Ripley's K
- [x] MTA時間帯別クラスタリング
- [x] クラスター × ビル属性クロス集計

### Notebook B に回すもの（予測的分析）
- [ ] 立地適応度スコア（需要/供給比）
- [ ] 出店候補地ランキング
- [ ] バックテスト（過去の出退店をスコアで再現）
- [ ] OSMnx歩行圏ポリゴン
- [ ] サードプレイスマトリクス（滞在型 vs テイクアウト分類モデル）

---

## セル数見積もり

| Section | コード | マークダウン | 計 |
|---|---|---|---|
| 0: Setup | 2 | 1 | 3 |
| 1: Hook | 2 | 1 | 3 |
| 2: Moran's I | 2 | 1 | 3 |
| 3: LISA | 2 | 1 | 3 |
| 4: NN + Ripley's K | 3 | 1 | 4 |
| 5: MTA Clustering | 3 | 1 | 4 |
| 6: Limitations | 0 | 2 | 2 |
| **合計** | **14** | **8** | **22** |

目標 22 cells、読了15-20分。Theme 0 の 23 cells とほぼ同規模。

---

## 必要なDataset

**既存の manhattan-cafe-wars Dataset を v2 として拡張する。**

新規Datasetを作ると紐付けが分散し、他のKagglerがnotebookを書く時の入口が2つに割れる。
1つのDatasetに集約し、Notebook A/B の両方が同じソースを参照する形にする。

### v2 で追加するファイル
- stores_enriched_v3.csv（171行 × 51カラム、全Join済み統合テーブル）
- manhattan_tracts_lisa.geojson（LISA map用のTract polygons + クラスター情報）
- mta_station_clusters.csv（123駅 × 時間帯別クラスター）

### v1 から引き続き同梱
- manhattan_starbucks_osm.csv（171店舗）
- manhattan_cafes_osm.csv（1,335カフェ）
- manhattan_mta_ridership_summary.csv（123駅）
