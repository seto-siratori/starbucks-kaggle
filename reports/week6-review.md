# Week 6 レビュー

作成日: 2026-03-13

---

## 実施したこと

| Day | タスク | 対象 |
|---|---|---|
| Day 1 | Notebook A 最終推敲 + Dataset v2 フォルダ準備 | テーマ2 |
| Day 2 | テーマ1 NLPプロトタイプ前半（テキスト前処理 + キーワード頻度分析） | テーマ1 |
| Day 3 | テーマ1 NLPプロトタイプ後半（LDAトピックモデリング + ヒーロー図） | テーマ1 |
| Day 4 | 店舗数時系列抽出（30年分） + 全米マクロデータ整備 | テーマ1 |
| Day 5 | Notebook B 構成設計（docs/notebook_b_outline.md） | テーマ2 |
| Day 6 | stores_enriched_v4 構築（需要/供給特徴量追加）+ Week 6レポート | テーマ2 |

---

## 分析結果サマリ

### テーマ1: NLPプロトタイプ

#### 手法選定

3手法を検討し、**キーワード頻度分析 + LDA** の組み合わせを採用。

| 手法 | 判定 | 理由 |
|---|---|---|
| キーワード頻度分析 | **採用** | 最もシンプルで解釈が明確。CEO交代・中国展開のタイミングが1年単位で追跡可能 |
| LDA トピックモデリング | **採用** | 847チャンク（文単位150語分割）で7トピック。30年のトピック構成変化が積み上げ面グラフで可視化できた |
| BERTopic / sentence-embedding | **不採用** | 30文書では不安定。LDAで十分なストーリーが見えたため追加コスト不要 |

#### キーワード分析の主要発見

| 発見 | 数字 |
|---|---|
| "coffee" の衰退 | FY1996: 348/10K語 → FY2025: 132/10K語（**62%減**） |
| "experience" の台頭 | FY1996: 0 → FY2023: 27/10K語（ピーク） |
| "partner" vs "employee" クロスオーバー | **FY2010** に "partner" が "employee" を逆転 |
| "china" のピーク | FY2018 に最高値（34/10K語）→ FY2019以降に後退 |
| "mobile" の出現 | FY2012まで完全にゼロ → FY2013初出 → FY2020-23にピーク |
| "digital" + "mobile" vs 店舗数 | **r = 0.90** (p < 0.001) |

#### LDAトピックの主要発見

7トピックで30年のアニュアルレポート言語を分解:

| トピック | 支配的な時代 | 解釈 |
|---|---|---|
| Store Operations | 全時代の基盤（20-39%） | コアビジネスの記述 |
| Supply Chain & Commodity | 安定（8-20%） | コーヒー調達リスク |
| Leadership & Governance | FY2001-2004に急増 | Sarbanes-Oxley法の開示要件変化 |
| Digital & Loyalty | FY2015以降に台頭（5%→14%） | モバイルオーダー/リワードプログラム |
| International & IP | FY1996-2000に17%、その後低下 | 初期の海外展開・知財記述 |
| **People, Culture & ESG** | **FY2020以降に爆増（<10%→25-30%）** | **最大の発見。COVID/人種問題/組合化の影響** |
| Product & Competition | FY1996-2000に27-34%、以降一貫して低下 | 「コーヒー会社」からの脱皮 |

**最大の発見**: Topic 5（People/ESG）がFY2020以降に <10% → 25-30% に急膨張。10-Kが「コーヒーの話」から「人と社会の話」に変質している。

#### 店舗数時系列

10-K Item 1テキストから30年分の店舗数を抽出。

| 指標 | FY1996 | FY2008 | FY2020 | FY2025 |
|---|---|---|---|---|
| 全世界合計 | 1,006 | 16,680 | 32,660 | 40,576 |
| ライセンス比率 | 7.5% | 44.7% | 49.1% | 49.3% |
| 海外比率 | 0.0% | 30.7% | 53.1% | 58.4% |

- FY2009が**唯一のマイナス成長**（-0.3%、800店閉鎖）
- 成長マイルストーン: 1K(1996) → 10K(2005) → 20K(2014) → 30K(2019) → 40K(2024)

#### 戦略言語 × 出店ペースの相関

| キーワード | vs 指標 | r値 |
|---|---|---|
| "china" | 海外店舗数 | **r = 0.52** (p < 0.01) |
| "digital"+"mobile" | 全店舗数 | **r = 0.90** (p < 0.001) |
| "experience" | 全店舗数 | **r = 0.95** (p < 0.001) |

### テーマ2: Notebook B 設計 + v4 データ構築

#### Notebook B 設計

タイトル: **"Where Should the 172nd Starbucks Go? Demand-Supply Gap Scoring for Manhattan (Reusable Template)"**

核: Location Fitness Score (LFS) = Demand Proxy Index / Supply Density

需要代理変数:
- MTA乗降客数（重み 0.50）
- 歩行者通行量（重み 0.25）— 36地点のNYC Bi-Annual Pedestrian Counts
- 居住人口密度（重み 0.25）

不採用: 世帯所得（r=0.03、Notebook Aで無相関確認済み）

#### stores_enriched_v4

| 指標 | v3 | v4 |
|---|---|---|
| 行数 | 171 | 171 |
| カラム数 | 51 | 63 |
| 追加カラム | — | Tract別需給スコア（10列）+ 歩行者カウント（2列） |

追加カラム:
- `tract_starbucks_count`, `tract_total_cafes`, `tract_competitor_cafes`
- `tract_mta_ridership`, `tract_avg_ped_count`, `tract_pop_density`
- `demand_proxy_index`, `supply_index`, `location_fitness_score`
- `tract_lisa_cluster`, `ped_count_nearest`, `ped_dist_m`

#### LFS プレビュー結果

**Under-served上位（出店候補）**:
- Census Tract 158.02 (LFS=3.14): スタバ1店、競合0、需要あり
- Census Tract 101 (LFS=3.09): スタバ2店、競合3だが需要が非常に高い
- Census Tract 145 (LFS=3.07): スタバ1店、競合1、需要に対して供給不足

**Over-served上位（カニバリリスク）**:
- Census Tract 94 (LFS=0.00): スタバ4店、競合8 — LISA High-High
- Census Tract 82 (LFS=0.10): スタバ4店、競合10 — LISA High-High

---

## 成果物一覧

### テーマ1

| ファイル | 内容 |
|---|---|
| data/interim/item1_basic_stats.csv | 30年分のテキスト基本統計 |
| data/interim/item1_keyword_timeseries.csv | 30年×64カラムのキーワード頻度 |
| data/interim/item1_lda_topic_proportions.csv | 30年×7トピックの年度別比率 |
| data/processed/sec-edgar/store_counts_timeseries.csv | 30年×16カラムの店舗数時系列 |
| reports/item1_keyword_trends.html | 戦略キーワード6種の時系列グラフ |
| reports/item1_phrase_trends.html | 複合フレーズ4種の時系列グラフ |
| reports/item1_text_stats.html | 文書長・語彙多様性の推移 |
| reports/item1_identity_shifts.html | アイデンティティ変化6種の時系列グラフ |
| reports/item1_lda_stacked_area.html | LDA 7トピック積み上げ面グラフ |
| reports/item1_lda_individual_topics.html | 7トピック個別推移グラフ |
| reports/item1_hero_chart.html | 4パネル統合ヒーロー図 |
| reports/store_count_timeline.html | 4パネル店舗数推移図 |
| reports/stores_vs_nlp.html | 3パネルNLP×店舗数対比図 |

### テーマ2

| ファイル | 内容 |
|---|---|
| notebooks/02_theme2/notebook_a_spatial_clustering.ipynb | Notebook A 推敲済み（Fig.番号追加、英文修正） |
| dataset-upload/v2/ | Dataset v2 アップロード用フォルダ（6ファイル + metadata.json） |
| docs/notebook_b_outline.md | Notebook B 構成設計書 |
| data/processed/stores_enriched_v4.csv | 171行×63カラム（v3 + 需給スコア + 歩行者） |
| data/interim/tract_demand_supply.csv | 309 Tract×需給スコア |

---

## Notebook A 推敲の変更点（Day 1）

| 変更 | 内容 |
|---|---|
| 図番号 | 全5図に Fig. 1〜5 を付番（タイトル・コメント・マークダウン参照すべて統一） |
| 英文修正 | 不自然な表現を修正、縮約形の統一 |
| pip install | geopandas を追加 |
| 全セル実行確認 | nbconvert --execute で26セル全通過（エラーゼロ） |

---

## テーマ0の公開状況

| 項目 | ステータス |
|---|---|
| Dataset | Private（電話番号認証待ち） |
| Notebook | Private（電話番号認証待ち） |
| 認証状況 | 未解決。4週間経過 |

---

## Week 7 でやるべきこと

### 優先度 P1（必須）

| タスク | 内容 |
|---|---|
| Notebook B コーディング | notebook_b_outline.md に基づき Section 0-7 を実装。stores_enriched_v4 + tract_demand_supply.csv を使用 |
| Kaggle公開（認証通過時） | Dataset v2 + Notebook A push → Internet ON → Run All → Public |

### 優先度 P2（できれば）

| タスク | 内容 |
|---|---|
| テーマ1 Notebook設計 | NLP分析 + 店舗数時系列のNotebook構成設計（docs/notebook_theme1_outline.md） |
| 歩行者カウントのTract空間補間 | 36地点→309 Tractへの IDW or Kriging 補間（Notebook B Section 2 の精度向上） |

### 優先度 P3（余裕があれば）

| タスク | 内容 |
|---|---|
| Kaggle directory.csv 取得 | バックテスト用の2017年時点店舗リスト |
| LinkNYCキオスク利用データ結合 | 需要代理変数の追加候補（1,224基のWi-Fi利用量） |
| 全米出店アニメーション設計 | store_counts_timeseries.csv + 州別データで出店密度の時系列マップ |

---

## リスクと注意事項

1. **Kaggle電話番号認証** — 4週間未解決。テーマ0・テーマ2ともに公開がブロックされている。新アカウント作成を本格的に検討すべき時期
2. **歩行者カウントのカバレッジ** — マンハッタン36地点のみ。309 Tractのうち多くが最寄りカウンタから1km以上離れている。空間補間の精度は限定的
3. **LFS の重み設定** — 売上データなしでは重みの「正解」が不明。感度分析でロバスト性を示す必要がある
4. **stores_enriched の版管理** — v1(44列) → v2(49) → v3(51) → v4(63) と拡張が続いている。Notebook A は v3 を使用、Notebook B は v4 を使用。Dataset に同梱するのは最新版のみ
