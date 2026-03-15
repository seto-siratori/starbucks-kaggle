# Week 4 レビュー

作成日: 2026-03-13

---

## 実施したこと

| Day | タスク | 対象 |
|---|---|---|
| Day 1 | SEC EDGAR 10-K 全量ダウンロード（30本、FY1996-FY2025） | テーマ1 |
| Day 2 | セクション分割パイプライン構築（src/edgar_parser.py） | テーマ1 |
| Day 3 | 全30本にItem 1抽出適用 → テキストコーパス完成 | テーマ1 |
| Day 4 | stores_enriched_v1.csv 構築（PLUTO + MTA + 競合密度） | テーマ2 |
| Day 5 | 品質検証 + ACS Census Tract結合 → stores_enriched_v2.csv | テーマ2 |
| Day 6 | 初期可視化（scatter_map）+ Week 4レポート | テーマ2 |

---

## 成果物一覧

### テーマ1: 10-K テキストコーパス

| 項目 | 値 |
|---|---|
| 対象 | SEC EDGAR 10-K Filing（FY1996-FY2025） |
| ファイル数 | **30本**（当初想定29本 + FY1998の10-K405） |
| 抽出成功率 | **100%（30/30）** |
| 抽出セクション | Item 1 (Business) |
| 文字数範囲 | 19,298 - 54,567 chars |
| 保存先 | data/processed/sec-edgar/item1_texts/ |
| サマリCSV | data/processed/sec-edgar/item1_summary.csv |

#### フォーマット別内訳

| フォーマット | 年度 | 本数 | 文字数範囲 |
|---|---|---|---|
| TXT（SGML） | FY1996-FY2000 | 5 | 19K-20K |
| HTML | FY2001-FY2018 | 18 | 27K-55K |
| XBRL | FY2019-FY2025 | 7 | 32K-45K |

#### パーサー（src/edgar_parser.py）

- `detect_format()`: 拡張子 + XBRL名前空間で3フォーマットを自動判定
- `_extract_item1_txt()`: SGML タグ除去 + 正規表現セクション分割
- `_extract_item1_html()`: BeautifulSoup → テキスト変換 → 正規表現セクション分割
- `_extract_item1_xbrl()`: BeautifulSoup（display:none除去） → 正規表現セクション分割
- `_find_item1_boundaries()`: HTML/XBRL共通のItem 1境界検出（TOCスキップロジック付き）

### テーマ2: stores_enriched_v2.csv

| 項目 | 値 |
|---|---|
| 行数 | **171店舗** |
| カラム数 | **49** |
| 保存先 | data/processed/stores_enriched_v2.csv |

#### カラム構成

| グループ | カラム数 | 内容 |
|---|---|---|
| OSM基本情報 | 17 | osm_id, name, addr_*, lat, lon 等 |
| PLUTO建物属性 | 12 | landuse, bldgclass, numfloors, yearbuilt, retailarea, assesstot 等 |
| MTA最寄り駅 | 4 | station_id, station_name, dist_m, avg_daily_ridership |
| 競合密度 | 11 | n_starbucks/dunkin/other_cafe × 250m/500m/1000m + nearest距離 |
| Census Tract (ACS) | 5 | tract_id, population, median_income, pct_walk_commute, pct_bachelors_plus |

#### Join品質サマリ

| Join | マッチ率 | 最大距離 | 中央値距離 | NULL |
|---|---|---|---|---|
| PLUTO (nearest) | 100% | 71.8m | 21.3m | numfloors:9, retailarea:8 |
| MTA (nearest) | 100% | 745m | 195m | 0 |
| 競合密度 (KDTree) | 100% | — | — | 0 |
| Census Tract (sjoin) | 100% | — | — | median_income:3 |

#### 異常値の原因

| 異常 | 件数 | 原因 |
|---|---|---|
| YearBuilt = 0 | 6 | 交通施設(U6)/公共空間(V1)。PLUTOの仕様 |
| RetailArea = 0 | 14 | PLUTO上で小売面積が分離計上されていないビル |
| NumFloors NULL | 9 | PLUTOに階数データなし（同上） |

---

## 初期可視化の所見

### scatter_map: 乗降客数 × 競合密度

- **乗降客数と競合密度の相関: r = 0.58** — 強い正の相関
- 上位20店（乗降客数）: 平均62店の競合（500m圏内）
- 下位20店: 平均26店
- **所得との相関: r = 0.03** — ほぼ無相関
- **所見**: スタバの立地選択は世帯所得よりも**人流（駅の乗降客数）に強く依存**。高乗降客エリアでは競合も密集するが、スタバはそこに集中出店している → ドミナント戦略の裏付け

保存先: reports/theme2_viz_ridership_competition.html

---

## テーマ0の公開状況

| 項目 | ステータス |
|---|---|
| Dataset | Private（電話番号認証待ち） |
| Notebook | Private（電話番号認証待ち） |
| 認証状況 | Kaggleに問い合わせ済み。返答待ち |

---

## 公開時点の数字

| 指標 | 値 |
|---|---|
| Dataset upvotes | — |
| Dataset views | — |
| Notebook upvotes | — |
| Notebook views | — |

*電話番号認証が通り次第、公開 → 数字記録*

---

## Week 5 でやるべきこと

### 優先度 P1（必須）

| タスク | 内容 |
|---|---|
| テーマ1 NLPプロトタイプ | 30年分のItem 1テキストでトピックモデリング or embedding時系列分析 |
| テーマ2 Notebook A 設計 | stores_enriched_v2を使ったドミナント戦略分析Notebookの構成設計 |
| Kaggle公開（認証通過時） | Dataset + Notebook Public化 → Internet ON → Run All確認 |

### 優先度 P2（できれば）

| タスク | 内容 |
|---|---|
| 店舗数時系列の抽出 | Item 1テキストからregexで年次店舗数を抽出 → 30年推移グラフ |
| 空間自己相関分析 | Moran's I / LISA で店舗密度のクラスタリング |
| MTA時間帯別乗降データ | 朝/昼/夜の人流パターン → 店舗タイプ（滞在型vsテイクアウト）との対応 |

### 優先度 P3（余裕があれば）

| タスク | 内容 |
|---|---|
| 全米出店アニメーション | Kaggle starbucks directory.csv + ACS州別人口で出店密度の時系列マップ |
| OSMnx歩行距離一括計算 | 171店×123駅のネットワーク距離（Phase 2） |

---

## リスクと注意事項

1. **Kaggle電話番号認証** — 引き続き未解決。テーマ0の公開がブロックされている
2. **NLPライブラリのKaggle互換性** — scikit-learn, gensim等がKaggle環境にプリインストールされているか要確認
3. **Item 1テキストの年代差** — FY1996-2000(~20K文字) vs FY2001以降(~30-55K文字)。テキスト量の差がNLP結果にバイアスをかける可能性
