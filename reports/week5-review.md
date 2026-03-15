# Week 5 レビュー

作成日: 2026-03-13

---

## 実施したこと

| Day | タスク | 対象 |
|---|---|---|
| Day 1 | 空間自己相関分析（Global Moran's I + LISA） | テーマ2 |
| Day 2 | 競合密度の空間パターン分析（最近接距離 + Ripley's K） | テーマ2 |
| Day 3 | MTA乗降データの時間帯別分析 + 駅クラスタリング | テーマ2 |
| Day 4 | Notebook A 構成設計（docs/notebook_a_outline.md） | テーマ2 |
| Day 5 | Notebook A コーディング前半（Section 0-3） | テーマ2 |
| Day 6 | Notebook A コーディング後半（Section 4-6）+ Week 5 レポート | テーマ2 |

---

## 分析結果サマリ

### 1. Global Moran's I（空間自己相関）

| 統計量 | 値 |
|---|---|
| Moran's I | **0.359** |
| Expected I (ランダム) | -0.003 |
| z-score | **11.26** |
| p-value | **< 0.001** |

**解釈**: スタバの出店密度に統計的に非常に有意な正の空間自己相関が存在。Census Tract単位で見て、スタバが多いエリアの隣もスタバが多い。ランダム配置の仮説は棄却（p < 0.001）。

### 2. LISA クラスター

| クラスター | Tract数 | 地理的集中 |
|---|---|---|
| High-High (ホットスポット) | 30 | Chelsea/Murray Hill に77%集中 |
| Low-Low (コールドスポット) | 5 | Upper Manhattan, Upper West/East Side |
| High-Low (外れ値) | 5 | 散在 |
| Low-High (ホットゾーン内の空白) | 9 | Chelsea/FiDi周辺 — 出店余地候補 |

### 3. 最近接距離分析

| 指標 | Starbucks | Dunkin' | 比率 |
|---|---|---|---|
| 同ブランド最近接距離 中央値 | **208m** | 294m | **1.41x** |
| 同ブランド最近接距離 平均値 | 279m | 329m | 1.18x |
| 200m以内の店舗割合 | 48% | — | — |

**解釈**: スタバはDunkin'より1.41倍密に自社同士を配置。48%の店舗が200m以内に別のスタバがある。ドミナント戦略の定量的証拠。

### 4. Ripley's K / Besag's L 関数

- 全距離帯（50m-2000m）で完全空間ランダム（CSR）を大幅に超過
- スタバのL値はDunkin'を全距離帯で上回る
- 200mでL=351 vs Dunkin' L=211、500mでL=999 vs 778

### 5. MTA時間帯別クラスタリング（K-means, K=4）

| クラスター | 駅数 | スタバ数 | AM比率 | PM比率 | 特徴 |
|---|---|---|---|---|---|
| Morning Peak (Residential) | 35 | 14 | 27.9% | 19.3% | 住宅地の通勤駅 |
| Balanced (Transit Hub) | 30 | 52 | 17.3% | 29.6% | 乗換駅 |
| Midday-Heavy (Tourism) | 32 | 58 | 11.1% | 28.9% | Times Sq, Herald Sq |
| Evening Peak (Office) | 26 | 47 | 7.5% | 38.3% | Rockefeller, Bryant Park |

**クラスター × ビル属性**:
- Office District: RetailArea中央値 10,000sqft、スタバ間隔 184m
- Residential: RetailArea中央値 4,965sqft、スタバ間隔 462m（2.5倍の差）

### 6. 「所得 vs 人流」の発見（Week 4からの継続）

| 相関 | r値 |
|---|---|
| 乗降客数 vs 競合密度（500m） | **r = 0.58** |
| 世帯年収 vs 競合密度（500m） | **r = 0.03** |

**解釈**: スタバの立地選択は世帯所得ではなく人流（駅乗降客数）に依存。

---

## Notebook A 完成度

| Section | 内容 | セル数 | 状態 |
|---|---|---|---|
| 0: Setup | pip install + pathlib + CSV読み込み | 3 | DONE |
| 1: Hook | scatter_map + 相関比較 | 4 | DONE |
| 2: Moran's I | Census Tract集計 + Global Moran's I | 4 | DONE |
| 3: LISA | Local Moran's I + choropleth map | 5 | DONE |
| 4: NN + Ripley's K | 最近接距離 + L関数 | 5 | DONE |
| 5: Template | 再利用可能関数 | 3 | DONE |
| 6: Limitations | 制約 + Next Steps | 2 | DONE |
| **合計** | | **26** | **100%** |

- ローカル全セル実行: **PASS**（エラーゼロ）
- Kaggle公開: **未実施**（Week 6で推敲後に公開予定）

**設計判断**: MTA時間帯別分析（Day 3）は Notebook A に含めない判断とした。理由: 26セルで既に上限に近く、時間帯別分析を追加すると30セルを超えて「15-25分で読める」原則を超過する。MTA分析はNotebook Bに回す。

---

## 成果物一覧

| ファイル | 内容 |
|---|---|
| data/processed/stores_enriched_v3.csv | 171行 × 51カラム（station_cluster追加） |
| data/interim/manhattan_tracts_lisa.geojson | LISA分析済みTractポリゴン |
| data/interim/mta_station_clusters.csv | 123駅の時間帯別クラスター |
| data/raw/mta_hourly_manhattan_q4_2024.csv | MTA時間帯別生データ |
| notebooks/02_theme2/notebook_a_spatial_clustering.ipynb | Notebook A 完成版（26セル） |
| docs/notebook_a_outline.md | Notebook A 構成設計書 |
| reports/station_hourly_clusters.html | 駅クラスタープロファイル図 |
| reports/nn_distance_distributions.html | 最近接距離分布図 |
| reports/ripley_k_function.html | Ripley's K関数図 |
| reports/lisa_cluster_map.html | LISA クラスターマップ |
| reports/landuse_map.html | LandUse色分け地図 |
| reports/theme2_viz_ridership_competition.html | 乗降客数×競合密度マップ |

---

## テーマ0の公開状況

| 項目 | ステータス |
|---|---|
| Dataset | Private（電話番号認証待ち） |
| Notebook | Private（電話番号認証待ち） |
| 認証状況 | 未解決。ユーザーからKaggleに問い合わせ済み |

---

## Week 6 でやるべきこと

### 優先度 P1（必須）

| タスク | 内容 |
|---|---|
| Notebook A 推敲 | マークダウン英文の推敲、図のキャプション統一、セル順序の最終確認 |
| Dataset v2 準備 | manhattan-cafe-wars に stores_enriched_v3.csv, geojson, clusters を追加 |
| Kaggle公開（認証通過時） | Dataset v2 + Notebook A push → Internet ON → Run All → Public |
| Notebook B 設計開始 | 立地適応度スコアリングの構成設計（docs/notebook_b_outline.md） |

### 優先度 P2（できれば）

| タスク | 内容 |
|---|---|
| テーマ1 NLPプロトタイプ | 30年分のItem 1テキストでトピックモデリング or embedding |
| 店舗数時系列の抽出 | Item 1テキストからregexで年次店舗数を抽出 |
| 全米出店アニメーション設計 | Kaggle directory.csv + ACS州別人口 |

### 優先度 P3（余裕があれば）

| タスク | 内容 |
|---|---|
| OSMnx歩行距離一括計算 | 171店×123駅のネットワーク距離 |
| 歩行者カウントデータ結合 | NYC Pedestrian Counts → stores_enriched |

---

## リスクと注意事項

1. **Kaggle電話番号認証** — 3週間未解決。テーマ0・テーマ2ともに公開がブロックされている。最悪の場合、新アカウント作成を検討
2. **Notebook A のKaggle互換性** — libpysal, esda がKaggle環境にプリインストールされているか未確認。pip install で対応できるはずだがInternet ON必須
3. **Dataset v2 のファイルサイズ** — geojsonの追加でDatasetサイズが増加。Kaggleの20GB制限には余裕があるが、ダウンロード速度への影響を確認
