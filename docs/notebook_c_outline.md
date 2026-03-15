# Notebook C — Data Pipeline & Quality Documentation

## メタ情報

- **タイトル案:** "Starbucks Data Pipeline: From SEC EDGAR & OSM to Analysis-Ready CSVs"
- **目的:** データの信頼性を示すドキュメントNotebook。「このデータ信頼できるの？」に答える
- **読者:** Notebook A/B/Theme 1 を見て「元データはどう作ったの？」と思った人
- **読了時間:** 10–15分
- **図の数:** 2–3本（最小限。テーブルとコードブロック主体）
- **Dataset参照:** `shiratoriseto/starbucks-30year-nlp-corpus` + `shiratoriseto/manhattan-cafe-wars`
- **Kaggle実行:** 可能（Section 2のEDGAR 1ファイルデモ + Section 3のOverpass APIデモのみ実行）

---

## Section 0 — Setup（1セル code + 1セル markdown）

**目的:** 依存パッケージのインストールとパス設定

**コード内容:**
```python
!pip install -q beautifulsoup4 requests pandas

import pandas as pd
from pathlib import Path
from IPython.display import display, HTML
```

**備考:**
- geopandasやplotlyは不要（分析Notebookではないため）
- beautifulsoup4はSection 2のEDGARパースデモに必要
- requestsはSection 2/3のAPI呼び出しに必要

---

## Section 1 — Data Architecture Overview（2セル markdown + 1セル code）

**目的:** プロジェクト全体のデータの流れを俯瞰する。2つのDataset × 4つのNotebookの対応関係

### 1.1 Dataset → Notebook 対応表（markdown）

| Dataset | Files | Used By |
|---------|-------|---------|
| **manhattan-cafe-wars** (8 files, 205KB) | manhattan_starbucks_osm.csv, manhattan_cafes_osm.csv, manhattan_mta_ridership_summary.csv, stores_enriched_v4.csv, tract_demand_supply.csv, manhattan_pedestrian_counts.csv, manhattan_tracts_lisa.geojson, mta_station_clusters.csv | Theme 0, Notebook A, Notebook B |
| **starbucks-30year-nlp-corpus** (4 files, 26KB) | store_counts_timeseries.csv, item1_keyword_timeseries.csv, item1_lda_topic_proportions.csv, item1_basic_stats.csv | Theme 1 (NLP) |

### 1.2 データフロー図（markdownテキスト図）

```
Raw Sources                    Pipeline                      Published Dataset
─────────────────────────────────────────────────────────────────────────────────
SEC EDGAR (30 10-K filings) → edgar_parser.py              → starbucks-30year-nlp-corpus
                              ├─ Item 1 extraction            ├─ store_counts_timeseries.csv
                              ├─ Keyword frequency             ├─ item1_keyword_timeseries.csv
                              ├─ LDA topic modeling            ├─ item1_lda_topic_proportions.csv
                              └─ Basic text stats              └─ item1_basic_stats.csv

OpenStreetMap (Overpass API) ─┐
MapPLUTO (NYC Open Data)     ─┤                             → manhattan-cafe-wars
MTA Ridership (NY Open Data) ─┼─ build_stores_enriched.py     ├─ manhattan_starbucks_osm.csv
Census ACS (Census Bureau)   ─┤   (KDTree nearest-neighbor)   ├─ manhattan_cafes_osm.csv
TIGER/Line Shapefiles        ─┤                                ├─ stores_enriched_v4.csv
NYC DOT Pedestrian Counts    ─┘                                ├─ tract_demand_supply.csv
                                                               └─ (+ 4 more files)
```

### 1.3 Data Source一覧テーブル（code: pd.DataFrame表示）

| Source | License | Access Method | Rate Limit | Rows/Files |
|--------|---------|---------------|------------|------------|
| SEC EDGAR | Public domain | HTTPS (sec.gov) | 10 req/sec, User-Agent required | 30 filings |
| OpenStreetMap | ODbL 1.0 | Overpass API | Soft limit (~10K nodes/query) | 171 + 1,335 nodes |
| MapPLUTO | NYC Open Data Terms | Bulk download (bytes.nyc) | None | ~43K Manhattan lots |
| MTA Ridership | NY Open Data Terms | Socrata API / bulk CSV | None (API key optional) | ~2.5M rows → 123 stations |
| Census ACS 2022 | Public domain | Census API / data.census.gov | 500 req/day (with key) | 309 Manhattan tracts |
| TIGER/Line | Public domain | Bulk download (census.gov) | None | ~4,900 NY tracts → 309 |
| NYC DOT Ped Counts | NYC Open Data Terms | NYC Open Data portal | None | 36 locations × 18 years |

---

## Section 2 — SEC EDGAR Pipeline Demo（3セル code + 2セル markdown）

**目的:** 10-K filing 1本のダウンロード → HTMLパース → Item 1抽出を実演。`edgar_parser.py` の主要関数を見せる

### 2.1 導入（markdown）
- SEC EDGARとは（CIK, filing index, User-Agent要件）
- 30年分のフォーマット変遷: txt(1996-2000) → html(2001-2018) → XBRL(2019-2025)

### 2.2 1ファイルデモ（code — 実行する）
```python
import requests
from bs4 import BeautifulSoup
import re

# Starbucks CIK: 0000829224
# Demo: FY2024 10-K (most recent complete year)
FILING_URL = "https://www.sec.gov/Archives/edgar/data/829224/..."
HEADERS = {"User-Agent": "StarbucksAnalysis research@example.com"}

response = requests.get(FILING_URL, headers=HEADERS)
print(f"Status: {response.status_code}, Size: {len(response.text):,} chars")

# --- Format detection ---
# detect_format() logic shown inline (not imported, for transparency)

# --- Item 1 extraction ---
# Boundary detection: "Item 1. Business" → "Item 1A."
# Show the regex patterns and explain TOC-skipping logic
```

**注意点:**
- 実際のFILING_URLはEdgar filing indexから取得する手順を見せる
- `edgar_parser.py` の `detect_format()`, `_find_item1_boundaries()`, `extract_item1()` のロジックをinlineで見せる（importではなく展開して透明性を確保）
- 抽出結果の先頭500文字と末尾500文字を表示し、境界検出が正しいことを確認

### 2.3 フル30年分のコード（code — 表示のみ、実行しない）
```python
# %%script echo "This cell is documentation only — not executed on Kaggle"
# Full pipeline: download all 30 filings and extract Item 1
# Estimated runtime: ~5 minutes (SEC EDGAR rate limit: 10 req/sec)
# ...
```

### 2.4 パース精度の検証（markdown + 小テーブル）
- 30ファイル中の抽出成功率: 30/30 (100%)
- 手動検証: FY1996, FY2009, FY2019, FY2025の4年分を目視確認
- 既知の問題: FY2003-2004のHTMLにネストしたテーブルがあり、一部書式が崩れるが内容は正確

---

## Section 3 — OSM Data Pipeline（2セル code + 2セル markdown）

**目的:** Overpass APIでマンハッタンのStarbucks + 競合カフェを取得する手順

### 3.1 Overpass APIクエリ（code — 実行する）
```python
import requests

# Overpass query: all cafes in Manhattan bounding box
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
query = """
[out:json][timeout:60];
area["name"="Manhattan"]["admin_level"="7"]->.manhattan;
(
  node["amenity"="cafe"](area.manhattan);
  way["amenity"="cafe"](area.manhattan);
);
out center;
"""

response = requests.post(OVERPASS_URL, data={"data": query})
data = response.json()
print(f"Total cafe nodes/ways: {len(data['elements'])}")
```

### 3.2 取得結果の検証（code + markdown）
- Starbucksの抽出: `brand == "Starbucks"` でフィルタ → 171店舗
- 公式店舗数との照合: Starbucks 10-K FY2024 Item 1 記載のNY Metro店舗数との比較
- OSMカバレッジの推定: 公式数 vs OSM数 → ~85%カバー
- brand_category分類ロジック: starbucks / dunkin / branded / independent

### 3.3 注意事項（markdown）
- OSMは継続的に更新されるため、取得時期によりデータが異なる
- 本プロジェクトのデータは2026年3月時点のスナップショット
- 再実行すると若干の差異が出る可能性あり（新規出店、閉店、OSM編集者による更新）

---

## Section 4 — Spatial Join Pipeline（2セル code + 2セル markdown）

**目的:** `build_stores_enriched.py` の3つのJoinの手順と精度検証

### 4.1 Join手法の概要（markdown）

3つのJoinはすべて **cKDTree nearest-neighbor** を使用:
- 座標系: WGS84 (EPSG:4326) → 簡易平面投影 (REF_LAT=40.75)
- マンハッタンスケールでの投影誤差: <0.5%

| Join | Source A | Source B | Method | Match距離 |
|------|----------|----------|--------|-----------|
| 1 | 171 Starbucks | ~43K MapPLUTO lots | 最近傍1件 | median 21.3m, max 71.8m |
| 2 | 171 Starbucks | 123 MTA stations | 最近傍1件 | median 195m, max 745m |
| 3 | 171 Starbucks | 1,164 competitor cafes | 半径カウント | 250m / 500m / 1000m |

### 4.2 コードの主要部分（code — 表示のみ）
- `build_stores_enriched.py` の `to_meters()`, KDTree構築, `query_ball_point()` の核心部分を展開
- 各Joinのsanity check（assert文）を見せる

### 4.3 Join精度の検証結果（markdown テーブル）

**Join 1: MapPLUTO**
| Metric | Value |
|--------|-------|
| Match率 | 171/171 (100%) |
| 距離中央値 | 21.3m |
| 距離最大値 | 71.8m |
| Commercial/Mixed land use率 | 84.8% (期待通り: Starbucksは商業区画に立地) |
| NULL率: numfloors | 9/171 (5.3%) |
| NULL率: retailarea, comarea | 8/171 (4.7%) |

**Join 2: MTA最寄り駅**
| Metric | Value |
|--------|-------|
| 500m以内のStarbucks | 164/171 (95.9%) |
| 距離中央値 | 195m |
| 距離最大値 | 745m (Upper East/West Sideの駅間が広いエリア) |

**Join 3: 競合密度**
| Radius | Avg Starbucks | Avg Dunkin' | Avg Other Cafes |
|--------|---------------|-------------|-----------------|
| 250m | 1.6 | 1.1 | 7.9 |
| 500m | 6.6 | 3.6 | 28.4 |
| 1000m | 21.2 | 11.4 | 93.6 |

---

## Section 5 — Data Quality Report（1セル code + 2セル markdown）

**目的:** `stores_enriched_v4.csv` 全63カラムの型・欠損・処理方針を一覧

### 5.1 全カラム品質テーブル（code: CSVから自動生成）

```python
# Load stores_enriched_v4 and generate quality report
df = pd.read_csv(DATA_DIR / "stores_enriched_v4.csv")
quality = pd.DataFrame({
    "column": df.columns,
    "dtype": df.dtypes.astype(str),
    "non_null": df.notnull().sum(),
    "null_count": df.isnull().sum(),
    "null_pct": (df.isnull().sum() / len(df) * 100).round(1),
    "sample": [str(df[c].dropna().iloc[0])[:40] if df[c].notnull().any() else "N/A" for c in df.columns],
})
display(HTML(quality.to_html(index=False)))
```

### 5.2 欠損値の処理方針（markdown テーブル）

| Column Group | NULL Count | Reason | Treatment |
|-------------|------------|--------|-----------|
| addr_street, addr_housenumber, addr_postcode | 18% | OSM contributors未入力 | そのまま保持（分析に不使用） |
| phone | 24% | OSM任意フィールド | そのまま保持 |
| opening_hours | 46% | OSM任意フィールド | そのまま保持 |
| pluto_numfloors | 9/171 (5.3%) | PLUTOにフロア数データなし | NaN保持、分析では中央値で代替可 |
| pluto_retailarea, comarea | 8/171 (4.7%) | PLUTOに床面積データなし | NaN保持 |
| tract_median_income | 3/171 (1.8%) | Census ACSでの秘匿処理 | NaN保持、分析ではtract除外 |

### 5.3 NLP Corpus品質（markdown テーブル）

| File | Rows | NULLs | Validation |
|------|------|-------|------------|
| store_counts_timeseries.csv | 30 | 0 | 合計値 = co + lic = us + intl を全行検証済み |
| item1_keyword_timeseries.csv | 30 | 0 | total_words > 0 を全行検証、per10k = raw / total × 10000 を再計算検証済み |
| item1_lda_topic_proportions.csv | 30 | 0 | 各行の7トピック合計 ≈ 1.0 (±0.01) を検証済み |
| item1_basic_stats.csv | 30 | 0 | words > 0, lexical_diversity = unique_words / words を検証済み |

---

## Section 6 — Reproducibility Guide（2セル markdown）

**目的:** ゼロから全データを再構築するためのチェックリスト

### 6.1 必要な外部アカウント/キー

| Service | Required? | Purpose | Getting Started |
|---------|-----------|---------|-----------------|
| SEC EDGAR | User-Agentヘッダのみ（APIキー不要） | 10-K filings download | sec.gov/os/accessing-edgar-data |
| Census API | APIキー推奨（なくても500 req/day） | ACS demographic data | api.census.gov/data/key_signup.html |
| Overpass API | 不要 | OSM cafe data | overpass-api.de |
| NYC Open Data | 不要 | MapPLUTO, Pedestrian Counts | data.cityofnewyork.us |
| NY Open Data | 不要 | MTA Ridership | data.ny.gov |

### 6.2 再構築チェックリスト

```
□ Step 1: SEC EDGAR (推定: 5分)
  └─ 30 filing URLsをEDGAR filing indexから取得
  └─ 10 req/sec制限を守って順次ダウンロード
  └─ edgar_parser.py で Item 1 抽出 → 30 txt files

□ Step 2: NLP Processing (推定: 10分)
  └─ Keyword frequency computation (compute_keyword_trends())
  └─ LDA: テキスト → 150-word chunks → gensim LDA (k=7, random_state=42)
  └─ Basic stats: word count, sentence count, lexical diversity
  └─ Store counts: Item 1テキストからの年次店舗数の手動抽出

□ Step 3: OSM Data (推定: 1分)
  └─ Overpass APIでマンハッタン内の全カフェ取得
  └─ brand_category分類 → CSV出力

□ Step 4: Supplementary Data (推定: 30分)
  └─ MapPLUTO bulk download (bytes.nyc, ~200MB)
  └─ MTA ridership CSV download + 集計 (Q4 2024)
  └─ Census ACS API → 309 tracts の人口/所得/通勤手段
  └─ TIGER/Line shapefiles → Census Tract polygons
  └─ NYC DOT Pedestrian Counts download

□ Step 5: Spatial Joins (推定: 2分)
  └─ build_stores_enriched.py 実行
  └─ v1 → v2 → v3 → v4 の順に拡張

□ Step 6: Validation (推定: 5分)
  └─ stores_enriched_v4: 171行 × 63カラム, NULL率確認
  └─ NLP CSV: 30行, 合計値整合性チェック
  └─ 公式店舗数 vs OSM店舗数の照合

Total estimated time: ~55分 (初回、ダウンロード込み)
```

### 6.3 既知の再現性リスク

| Risk | Impact | Mitigation |
|------|--------|------------|
| OSMデータは日々更新される | 店舗数が ±5 程度変動する可能性 | 本プロジェクトは2026年3月スナップショット。Datasetに固定版を同梱 |
| LDA topic modelのrandom_state | 同じseedでもgensimバージョン差で微妙にずれる | topic proportions CSVをDatasetに同梱し、再学習は不要にした |
| SEC EDGAR のURL構造変更 | filing URLが変わる可能性（稀） | CIKベースのfiling index API は安定。直リンクよりindex経由を推奨 |
| Census ACS年次更新 | 2023版リリース後に数値が変わる | 本プロジェクトはACS 2022 5-Year Estimates固定 |

---

## セル構成まとめ

| Section | Markdown | Code | 実行する？ | 内容 |
|---------|----------|------|-----------|------|
| 0 Setup | 1 | 1 | Yes | pip install + imports |
| 1 Architecture | 2 | 1 | Yes | データフロー図 + source テーブル |
| 2 EDGAR Demo | 2 | 3 | **1本だけ実行 / 1本は表示のみ** | 1ファイルDL→パース実演 + フル30年コード提示 |
| 3 OSM Pipeline | 2 | 2 | **1本だけ実行** | Overpassクエリ実演 + 検証 |
| 4 Spatial Join | 2 | 2 | **表示のみ** | build_stores_enriched.py のコア部分 |
| 5 Data Quality | 2 | 1 | Yes | 63カラム品質レポート自動生成 |
| 6 Reproducibility | 2 | 0 | — | チェックリスト + リスクテーブル |
| **合計** | **~13** | **~10** | | **~23セル** |

---

## Kaggle実行の注意点

1. **Section 2 (EDGAR):** 1ファイルのみダウンロード（~30秒）。30ファイルはコード提示のみ
2. **Section 3 (OSM):** Overpass APIは通常Kaggleから到達可能だが、タイムアウトのリスクあり。`enable_internet: true` 必須
3. **Section 4 (Spatial Join):** MapPLUTOは200MBあるためKaggle上でのダウンロードは非現実的 → コード展示のみ
4. **Section 5 (Quality Report):** Dataset内のCSVを読むだけなので問題なし

## 既存コードの活用

| 既存ファイル | 使い方 |
|-------------|--------|
| `src/edgar_parser.py` | Section 2でロジックをinline展開して見せる（importではなく中身を見せる） |
| `src/build_stores_enriched.py` | Section 4でKDTree join部分を抜粋展開 |
| Theme 1 Notebook `compute_keyword_trends()` | Section 2で言及（再掲はしない、リンクで参照） |
