# データソース棚卸し表 (Data Sources Inventory)

最終更新: 2026-03-12

---

## 1. Starbucks 店舗位置データ (Kaggle)

### 1-A. Starbucks Locations Worldwide (公式)

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Locations Worldwide |
| 提供元 | Starbucks (Kaggle公式アカウント) |
| URL | https://www.kaggle.com/datasets/starbucks/store-locations |
| 内容 | 全世界のStarbucks全店舗の店名・オーナーシップ形態・所在地 |
| 主なカラム | Brand, Store Number, Store Name, Ownership Type, Street Address, City, State/Province, Country, Postcode, Phone Number, Timezone, Longitude, Latitude |
| 粒度 | 店舗単位 |
| 時点 | 2017年2月時点のスナップショット |
| ファイル形式 | CSV (ZIP圧縮) |
| ライセンス | Unknown（Kaggle上で「Unknown」と明記） |
| ライセンス原文URL | https://www.kaggle.com/datasets/starbucks/store-locations （メタデータ: "license":{"name":"Unknown","url":""} ） |
| ライセンス原文 | Kaggle上のライセンス欄: "Unknown" / データ出典: "This data was scraped from the Starbucks store locator webpage by Github user chrismeller" / GitHub元リポジトリ(chrismeller/StarbucksLocations): LICENSEファイルなし・リポジトリはアーカイブ済み |
| 再配布可否 | **グレー**（ライセンス不明。Starbucks Store LocatorからのスクレイピングデータでありStarbucks社の利用規約に抵触する可能性あり） |
| 検証日 | 2026-03-12 |
| 備考 | 約25,600店舗。テーマ1の30年アニメには開店年が無いため不十分 → 10-Kから店舗数推移を補完する必要あり。**再配布リスクあり：元データがスクレイピング由来でライセンス未設定** |

### 1-B. Starbucks Store Location 2023

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Store Location 2023: Coffee Giant Growth |
| 提供元 | omarsobhy14 (Kaggleユーザ) |
| URL | https://www.kaggle.com/datasets/omarsobhy14/starbucks-store-location-2023 |
| 内容 | 2023年時点のStarbucks全世界店舗位置 |
| 粒度 | 店舗単位 |
| 時点 | 2023年 |
| ファイル形式 | CSV |
| ライセンス | "Reddit API Terms"（Kaggle上の表記。明らかに誤設定） |
| ライセンス原文URL | https://www.kaggle.com/datasets/omarsobhy14/starbucks-store-location-2023 （メタデータ: "license":{"name":"Reddit API Terms"} ） |
| ライセンス原文 | ライセンス欄に「Reddit API Terms」と設定されているが、Starbucksデータとは無関係であり、投稿者の設定ミスと思われる。実際のデータ出典・取得方法の記載なし |
| 再配布可否 | **グレー**（ライセンス誤設定。データ出典不明） |
| 検証日 | 2026-03-12 |
| 備考 | 1-Aとの差分で6年分の出退店分析が可能。**ライセンスが明らかに誤設定されており信頼性に問題あり** |

### 1-C. Starbucks Locations Worldwide 2021 version

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Locations Worldwide 2021 version |
| 提供元 | kukuroo3 (Kaggleユーザ) |
| URL | https://www.kaggle.com/datasets/kukuroo3/starbucks-locations-worldwide-2021-version |
| 内容 | 2021年時点の全世界店舗位置 |
| 粒度 | 店舗単位 |
| 時点 | 2021年 |
| ファイル形式 | CSV |
| ライセンス | 要確認（Kaggleページで未確認） |
| ライセンス原文URL | https://www.kaggle.com/datasets/kukuroo3/starbucks-locations-worldwide-2021-version |
| ライセンス原文 | 未取得。1-Aと同じくスクレイピング由来の可能性が高い |
| 再配布可否 | **グレー** |
| 検証日 | 2026-03-12 |

---

## 2. SEC EDGAR — Starbucks 10-K年次報告書

| 項目 | 内容 |
|------|------|
| 正式名称 | SEC EDGAR Filing System — Starbucks Corporation 10-K |
| 提供元 | U.S. Securities and Exchange Commission (SEC) |
| URL (EDGAR検索) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000829224&type=10-K&dateb=&owner=include&count=40 |
| URL (EDGAR API) | https://data.sec.gov/ |
| URL (Full-Text Search API) | https://efts.sec.gov/LATEST/search-index?q=%22starbucks%22&dateRange=custom&startdt=1993-01-01&enddt=2025-12-31&forms=10-K |
| CIK番号 | 0000829224 |
| 内容 | 年次報告書 (10-K)。事業概要、店舗数推移、財務諸表、MD&A、リスクファクター等 |
| 粒度 | 会計年度 (Starbucksは9月末決算) |
| 時間範囲 | 1993年〜最新 (FY2024は2024年9月29日決算、2024年11月20日提出) |
| ファイル形式 | HTML, XBRL (JSON via API), PDF |
| ライセンス | パブリック情報（公的記録） |
| ライセンス原文URL | https://www.sec.gov/about/privacy-information （「Website Dissemination」セクション） |
| ライセンス原文 | "Information presented on sec.gov is considered public information and may be copied or further distributed by users of the web site without the SEC's permission. Please consider appropriate citation to the SEC as the source." |
| 再配布可否 | 可（出典明記推奨） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ1のNLP分析の主要ソース。XBRL Company Facts APIでJSON一括取得可能。Full-Text Search APIで2001年以降のフルテキスト検索可。User-Agentヘッダにメールアドレス記載が必要 |

---

## 3. Starbucks アニュアルレポート / IR

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Annual Reports |
| 提供元 | Starbucks Corporation Investor Relations |
| URL | https://investor.starbucks.com/financials/annual-reports/default.aspx |
| 内容 | 年次報告書PDF (デザイン版)。Letter to Shareholders、ビジョンステートメント、戦略サマリー含む |
| 粒度 | 会計年度 |
| 時間範囲 | 要確認 (直近数年分は確実に掲載) |
| ファイル形式 | PDF |
| ライセンス | 著作権はStarbucks社 |
| ライセンス原文URL | https://investor.starbucks.com/financials/annual-reports/default.aspx （※403でアクセス不可。企業著作物として再配布不可と判断） |
| ライセンス原文 | 企業が作成・発行するアニュアルレポートであり、著作権はStarbucks Corporationに帰属。分析目的の引用はフェアユース範囲だが、PDF自体の再配布は不可 |
| 再配布可否 | **不可**（notebookで取得手順のみ記載） |
| 検証日 | 2026-03-12 |
| 備考 | NLP分析には10-K (SEC EDGAR)を優先使用。Annual Reportは補完資料。FY2024版PDF: https://s203.q4cdn.com/326826266/files/doc_financials/2024/ar/Starbucks-Fiscal-2024-Annual-Report.pdf |

---

## 4. NYC Open Data

### 4-A. Bi-Annual Pedestrian Counts

| 項目 | 内容 |
|------|------|
| 正式名称 | Bi-Annual Pedestrian Counts |
| 提供元 | NYC Department of Transportation (DOT) |
| URL | https://data.cityofnewyork.us/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h |
| 内容 | 市内114地点（小売コリドー中心）の歩行者カウント |
| 粒度 | 地点 × 時間帯 (5月・9月の年2回計測) |
| 時間範囲 | 要確認 (複数年蓄積) |
| ファイル形式 | CSV, JSON (API), Shapefile |
| ライセンス | NYC Open Data (制限なし) |
| ライセンス原文URL | https://opendata.cityofnewyork.us/faq/ |
| ライセンス原文 | "Are there restrictions on how I can use Open Data?" → "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data." |
| 再配布可否 | 可 |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2の需要代理変数として使用。マンハッタン内の地点数を要確認。最終更新: 2025年1月 |

### 4-B. Building Footprints

| 項目 | 内容 |
|------|------|
| 正式名称 | Building Footprints |
| 提供元 | NYC Office of Technology & Innovation (OTI) |
| URL | https://data.cityofnewyork.us/City-Government/BUILDING/5zhs-2jue |
| 内容 | 建物フットプリント (外周ポリゴン)。BIN, BBL, 地上高、屋根高、建設年、Feature Type含む |
| 粒度 | 建物単位 |
| 時間範囲 | 日次更新 |
| ファイル形式 | GeoJSON, Shapefile, CSV |
| ライセンス | NYC Open Data (制限なし) |
| ライセンス原文URL | https://opendata.cityofnewyork.us/faq/ |
| ライセンス原文 | "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data." |
| 再配布可否 | 可 |
| 検証日 | 2026-03-12 |
| 備考 | BBLでMapPLUTOとジョイン可能。テーマ2のビル属性分析に使用 |

### 4-C. PLUTO / MapPLUTO

| 項目 | 内容 |
|------|------|
| 正式名称 | Primary Land Use Tax Lot Output (PLUTO) / MapPLUTO |
| 提供元 | NYC Department of City Planning (DCP) |
| URL (現行版) | https://www.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page |
| URL (新ページ) | https://www.nyc.gov/content/planning/pages/resources/datasets/mappluto-pluto-change |
| URL (NYC Open Data) | https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks |
| 内容 | 税区画 (tax lot) 単位の土地利用・建物特性。70以上のフィールド：用途区分、建物面積、建築年、階数、容積率、ゾーニング等 |
| 粒度 | 税区画 (Borough-Block-Lot) |
| 時間範囲 | 定期更新 (アーカイブあり) |
| ファイル形式 | CSV, Shapefile, File Geodatabase |
| ライセンス | NYC Open Data (2013年にライセンス制限撤廃、自由利用) |
| ライセンス原文URL | https://opendata.cityofnewyork.us/faq/ |
| ライセンス原文 | "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data." |
| 再配布可否 | 可 |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2の立地適応度評価の中核データ。BBLキーでBuilding Footprintsとジョイン。問い合わせ: DCPOpendata@planning.nyc.gov |

---

## 5. MTA 改札データ / 地下鉄乗降客数

### 5-A. MTA Subway Turnstile Usage Data (レガシー)

| 項目 | 内容 |
|------|------|
| 正式名称 | MTA Subway Turnstile Usage Data |
| 提供元 | Metropolitan Transportation Authority (MTA) |
| URL | https://web.mta.info/developers/turnstile.html |
| 内容 | 改札機ごとの累積入退場カウンター |
| 粒度 | 改札機 (C/A + Unit + SCP) × 4時間ブロック |
| 時間範囲 | 2010年〜2024年 (アーカイブ済、更新停止) |
| ファイル形式 | CSV (週次ファイル) |
| ライセンス | OPEN NY Terms of Use (制限なし) |
| ライセンス原文URL | https://data.ny.gov/dataset/OPEN-NY-Terms-Of-Use/77gx-ii52 |
| ライセンス原文 | "So long as you are not doing anything malicious with NYS data, you may use it as you wish, subject to no other requirements." / "do not contain restrictions requiring members of the public to use attribution, to re-post the license terms with any re-uses of the data, to impose share-alike or technical restrictions, nor require the public to obtain pre-approval before re-use of the data" |
| 再配布可否 | 可（帰属表示すら不要） |
| 検証日 | 2026-03-12 |
| 備考 | 累積カウンター形式のため差分計算が必要。異常値クレンジング要。レガシーフォーマット |

### 5-B. MTA Subway Hourly Ridership (新フォーマット)

| 項目 | 内容 |
|------|------|
| 正式名称 | MTA Subway Hourly Ridership: 2020-2024 / Beginning 2025 |
| 提供元 | MTA |
| URL (2020-2024) | https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-2020-2024/wujg-7c2s |
| URL (2025〜) | https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-2025/5wq4-mkjj |
| 内容 | 駅複合体 (station complex) ごとの時間別乗降客数 |
| 粒度 | 駅複合体 × 1時間 |
| 時間範囲 | 2022年2月〜現在 |
| ファイル形式 | CSV (Open Data NY API対応) |
| ライセンス | OPEN NY Terms of Use (制限なし) |
| ライセンス原文URL | https://data.ny.gov/dataset/OPEN-NY-Terms-Of-Use/77gx-ii52 |
| ライセンス原文 | "So long as you are not doing anything malicious with NYS data, you may use it as you wish, subject to no other requirements." |
| 再配布可否 | 可（帰属表示すら不要） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2の歩行者流動代理変数として最適。旧turnstileデータより高品質。Origin-Destination推計データセットも2024年7月公開 |

---

## 6. US Census — ACS / 人口データ

### 6-A. American Community Survey (ACS) 5-Year Estimates

| 項目 | 内容 |
|------|------|
| 正式名称 | American Community Survey 5-Year Data |
| 提供元 | U.S. Census Bureau |
| URL (API) | https://www.census.gov/data/developers/data-sets/acs-5year.html |
| URL (data.census.gov) | https://data.census.gov/ |
| 内容 | 人口、世帯収入、年齢構成、人種、教育、通勤手段、住居等の社会経済統計 |
| 粒度 | Census Tract, Block Group, ZIP Code Tabulation Area (ZCTA), County等 |
| 時間範囲 | 2009年〜2024年 (5年推計) |
| ファイル形式 | JSON (API), CSV (bulk download) |
| ライセンス | 米国政府データ（API利用規約あり） |
| ライセンス原文URL | https://www.census.gov/data/developers/about/terms-of-service.html |
| ライセンス原文 | "The U.S. Census Bureau offers some of its public data in machine-readable format via an Application Programming Interface. This service is offered subject to your acceptance of the terms and conditions contained herein." / 利用表示義務: "This product uses the Census Bureau Data API but is not endorsed or certified by the Census Bureau." / データ改変時: "You may not modify or falsely represent content accessed through the API and still claim the source is the Census Bureau." |
| 再配布可否 | 可（出典表示義務あり・個人特定禁止） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ1: ZIPコード別人口で出店密度の正規化。テーマ2: Census Tract別の所得・人口をマンハッタン空間分析に使用。API keyは無料取得可 (https://api.census.gov/data/key_signup.html) |

### 6-B. American Community Survey (ACS) 1-Year Estimates

| 項目 | 内容 |
|------|------|
| 正式名称 | American Community Survey 1-Year Data |
| 提供元 | U.S. Census Bureau |
| URL | https://www.census.gov/data/developers/data-sets/acs-1year.html |
| 内容 | 同上 (ただし人口65,000以上の地域のみ) |
| 粒度 | County, MSA, State等 (小地域なし) |
| 時間範囲 | 2005年〜2024年 |
| ファイル形式 | JSON (API), CSV |
| ライセンス | 米国政府データ（ACS 5-Yearと同じAPI利用規約） |
| ライセンス原文URL | https://www.census.gov/data/developers/about/terms-of-service.html |
| ライセンス原文 | （6-Aと同一） |
| 再配布可否 | 可（出典表示義務あり・個人特定禁止） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ1の時系列分析で経年比較に有用。Tract粒度が必要なテーマ2では5-Year版を使用 |

---

## 7. TIGER/Line Shapefiles

| 項目 | 内容 |
|------|------|
| 正式名称 | TIGER/Line Shapefiles |
| 提供元 | U.S. Census Bureau |
| URL (メインページ) | https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html |
| URL (Webインタフェース) | https://www.census.gov/cgi-bin/geo/shapefiles/index.php |
| 内容 | 行政境界 (州・郡・tract・block group)、道路ネットワーク、水系、鉄道等のジオメトリ |
| 粒度 | 各レイヤーによる (Census Tract, County, State, Block Group等) |
| 時間範囲 | 年次更新 (最新は2025年版、2025年9月リリース) |
| ファイル形式 | Shapefile (.shp/.dbf/.shx/.prj) |
| ライセンス | 米国政府データ（Census Bureauポリシー準拠） |
| ライセンス原文URL | https://www.census.gov/data/developers/about/terms-of-service.html |
| ライセンス原文 | （6-Aと同一のCensus Bureau利用規約が適用） |
| 再配布可否 | 可（出典表示義務あり） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ1: 全米地図ベースマップ。テーマ2: マンハッタンCensus Tractポリゴン。ACSデータとGEOIDでジョイン |

---

## 8. OpenStreetMap

### 8-A. Geofabrik Extracts (バルクダウンロード)

| 項目 | 内容 |
|------|------|
| 正式名称 | Geofabrik OpenStreetMap Data Extracts |
| 提供元 | Geofabrik GmbH / OpenStreetMap Contributors |
| URL (US全体) | https://download.geofabrik.de/north-america/us.html |
| URL (ニューヨーク州) | https://download.geofabrik.de/north-america/us/new-york.html |
| 内容 | 道路ネットワーク、建物、POI (カフェ、店舗等) の地理データ |
| 粒度 | ノード/ウェイ/リレーション |
| 時間範囲 | 日次更新スナップショット |
| ファイル形式 | .osm.pbf, .shp.zip |
| ライセンス | Open Database License (ODbL) 1.0 |
| ライセンス原文URL | https://www.openstreetmap.org/copyright / https://opendatacommons.org/licenses/odbl/summary/ |
| ライセンス原文 | "You are free to copy, distribute, transmit and adapt our data, as long as you credit OpenStreetMap and its contributors." / "If you alter or build upon our data, you may distribute the result only under the same license." |
| 再配布可否 | 可（条件あり: 帰属表示必須 + 派生DBは同一ライセンス） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2: OSMnxでの道路ネットワーク分析に使用。Overpass APIより一括取得の方が安定 |

### 8-B. Overpass API (クエリベース)

| 項目 | 内容 |
|------|------|
| 正式名称 | Overpass API |
| 提供元 | OpenStreetMap Community |
| URL (API) | https://overpass-api.de/ |
| URL (Overpass Turbo) | https://overpass-turbo.eu/ |
| 内容 | OSMデータのオンデマンドクエリ。特定エリア・タグのPOI抽出可 |
| 粒度 | ノード/ウェイ/リレーション |
| ファイル形式 | JSON, XML, CSV |
| ライセンス | ODbL 1.0 |
| ライセンス原文URL | https://www.openstreetmap.org/copyright / https://opendatacommons.org/licenses/odbl/summary/ |
| ライセンス原文 | （8-Aと同一） |
| 再配布可否 | 可（条件あり: 帰属表示必須 + 派生DBは同一ライセンス） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2のPOIデータ取得に使用。クエリ例: `node["amenity"="cafe"](bbox);` で競合カフェ抽出。レート制限あり、大量取得はGeofabrikを推奨 |

---

## 9. NYC TLC タクシー/配車サービス旅行データ

| 項目 | 内容 |
|------|------|
| 正式名称 | TLC Trip Record Data |
| 提供元 | NYC Taxi and Limousine Commission (TLC) |
| URL | https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page |
| URL (AWS) | https://registry.opendata.aws/nyc-tlc-trip-records-pds/ |
| URL (Taxi Zone Shapefile) | https://data.cityofnewyork.us/Transportation/NYC-Taxi-Zones/d3c5-ddgc |
| 内容 | Yellow Taxi / Green Taxi / FHV (Uber, Lyft等) の乗降地点、時刻、距離、運賃 |
| 粒度 | トリップ単位。位置はTaxi Zone ID (2016年7月以降、それ以前は緯度経度) |
| 時間範囲 | 2009年1月〜現在 (月次更新) |
| ファイル形式 | Parquet |
| ライセンス | NYC Open Data（NYC.gov Terms of Use準拠） |
| ライセンス原文URL | https://opendata.cityofnewyork.us/faq/ / https://registry.opendata.aws/nyc-tlc-trip-records-pds/ |
| ライセンス原文 | "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data." (NYC Open Data FAQ) / AWS Registry上のライセンスリンク先もNYC.gov Terms of Use |
| 再配布可否 | 可 |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2の需要代理変数。マンハッタンのTaxi Zone別乗降数で地域活性度を推定。データ量大 (年間数億行)、Parquet + DuckDB/Polarsでの処理推奨 |

---

## 10. POIデータ — 競合コーヒーショップ

### 10-A. OpenStreetMap経由

| 項目 | 内容 |
|------|------|
| 正式名称 | OpenStreetMap POI (amenity=cafe) |
| 提供元 | OpenStreetMap Contributors |
| 取得方法 | Overpass API or Geofabrik extract → osmium/osm2pgsql でフィルタ |
| 内容 | カフェ・コーヒーショップのPOI (名称、ブランド、座標) |
| タグ例 | `amenity=cafe`, `cuisine=coffee_shop`, `brand=Dunkin'`, `brand=Blue Bottle Coffee` |
| 粒度 | POI (ノード) 単位 |
| ファイル形式 | JSON (Overpass), PBF (Geofabrik) |
| ライセンス | ODbL 1.0 |
| 再配布可否 | 可 (ODbL準拠) |
| 備考 | マンハッタン内の競合店 (Dunkin', Peet's, Blue Bottle, Gregory's, 独立系) を抽出。OSMの網羅性は地域により差があるが、マンハッタンは充実度が高い |

### 10-B. Kaggle — Foursquare / Yelp系データセット

| 項目 | 内容 |
|------|------|
| 正式名称 | 要確認 (Foursquare NYC POI等) |
| 提供元 | Kaggle上の各種投稿者 |
| URL | 要確認 |
| 内容 | NYC近辺のPOIデータ (レストラン、カフェ等) |
| ライセンス | データセットごとに異なる、要確認 |
| 再配布可否 | 要確認 |
| 備考 | OSMで十分なカバレッジが得られない場合の補完候補 |

---

## 11. BLS 経済データ

### 11-A. Quarterly Census of Employment and Wages (QCEW)

| 項目 | 内容 |
|------|------|
| 正式名称 | Quarterly Census of Employment and Wages (QCEW) |
| 提供元 | U.S. Bureau of Labor Statistics (BLS) |
| URL (メイン) | https://www.bls.gov/cew/ |
| URL (ダウンロード) | https://www.bls.gov/cew/downloadable-data-files.htm |
| URL (API) | https://www.bls.gov/bls/api_features.htm |
| 内容 | 産業別の雇用者数・賃金。NAICS産業分類コード別 |
| 粒度 | County, MSA, State, National × 産業 (NAICS 6桁まで) |
| 時間範囲 | 1990年〜現在 (NAICS分類、四半期更新) |
| ファイル形式 | CSV |
| ライセンス | パブリックドメイン (米国政府データ) |
| ライセンス原文URL | https://www.bls.gov/opub/copyright-information.htm （※BLSのボット対策で自動取得不可。ブラウザで確認推奨） |
| ライセンス原文 | 「労働統計局（BLS）は連邦政府の機関であり、紙媒体および電子媒体で公開するすべてのものは、以前に著作権で保護されていた写真やイラストを除き、パブリックドメインに属します。特定の許可なく、当社のパブリックドメイン資料を自由にご利用いただけますが、出典として米国労働統計局を引用していただくようお願い申し上げます。」 |
| 再配布可否 | 可（出典表示推奨・ロゴ使用禁止） |
| 検証日 | 2026-03-12 |
| 備考 | テーマ2: マンハッタン (New York County FIPS 36061) のオフィスワーカー密度推定。NAICS 7225 (Restaurants and Other Eating Places) で飲食業雇用も取得可能 |

---

## ライセンス・再配布の整理サマリー

| データソース | ライセンス | 再配布 | Kaggle Dataset同梱 |
|---|---|---|---|
| Kaggle Starbucks店舗 (3件) | Unknown / グレー | グレー | **同梱しない（取得手順のみ記載）** |
| SEC EDGAR 10-K | パブリック情報 | 可（出典明記推奨） | 可 |
| Starbucks Annual Report PDF | 著作権あり | 不可 | 取得手順のみ記載 |
| NYC Open Data (歩行者/建物/PLUTO) | NYC Open Data (制限なし) | 可 | 可 |
| MTA Turnstile / Hourly Ridership | OPEN NY (制限なし) | 可 | 可 |
| US Census ACS | 米国政府データ | 可（出典表示必須） | 可 |
| TIGER/Line Shapefiles | 米国政府データ | 可（出典表示必須） | 可 |
| OpenStreetMap | ODbL 1.0 | 可（帰属表示+同一ライセンス必須） | 可（ODbL条件遵守） |
| NYC TLC Trip Data | NYC Open Data | 可 | 可（サイズ注意） |
| BLS QCEW | パブリックドメイン | 可（出典表示推奨） | 可 |

---

## データ方針（2026-03-12 確定）

### 基本方針
- **再配布OKなデータのみDatasetに同梱**
- **グレー/不可のデータはnotebookに取得手順を記載し、同梱しない**
- これにより、ライセンス違反リスクをゼロにする

### Starbucks店舗位置データの方針
- Kaggle上の店舗データ（1-A/1-B/1-C）はライセンスがグレーのため**Datasetに同梱しない**
- テーマ2: **OSM brand=Starbucks をメインソース**として使用（ODbL、再配布OK）
- テーマ1: 地理的位置はKaggleデータを使うが同梱せず、**notebookにダウンロード手順を記載**
- テーマ1: 店舗数の時系列推移は**SEC EDGAR 10-K**から取得（再配布OK）
- OSMデータをバックアップとして用意し、Kaggleデータ消失リスクに備える

---

## テーマ別 データマッピング（方針確定版）

### テーマ1: 全米30年空間アニメーション + NLP

| 分析要素 | 主データソース | 同梱 | 補完データ |
|---|---|---|---|
| 店舗数推移 (年次) | SEC EDGAR 10-K (Item 1, Properties) | 可 | — |
| 店舗位置 (地理) | Kaggle Starbucks Locations | **不可（手順記載）** | OSM (brand=Starbucks) |
| 全米ベースマップ | TIGER/Line Shapefiles | 可 | — |
| 人口正規化 | ACS 5-Year (ZIP/County) | 可 | — |
| NLPテキスト | SEC EDGAR 10-K HTML/XBRL | 可 | Annual Report PDF (手順記載) |

### テーマ2: マンハッタンドミナント戦略分析

| 分析要素 | 主データソース | 同梱 | 補完データ |
|---|---|---|---|
| Starbucks店舗位置 | **OSM (brand=Starbucks)** | 可 | Kaggle (手順記載) |
| 競合店舗位置 | OSM (amenity=cafe, Manhattan bbox) | 可 | — |
| 歩行者流動 | NYC Bi-Annual Pedestrian Counts | 可 | MTA Hourly Ridership |
| 地下鉄乗降客数 | MTA Subway Hourly Ridership | 可 | MTA Turnstile (レガシー) |
| ビル属性・用途 | MapPLUTO | 可 | Building Footprints |
| タクシー/配車需要 | NYC TLC Trip Data | 可 | — |
| 人口・所得 | ACS 5-Year (Census Tract) | 可 | — |
| 就業者密度 | BLS QCEW (New York County) | 可 | ACS通勤データ |
| 道路ネットワーク | OSM (via OSMnx) | 可 | — |
| 行政境界 | TIGER/Line (Census Tract) | 可 | — |

---

## ギャップ分析: 追加データソース候補 (2026-03-12 調査)

以下は既存棚卸し表で未カバーだったデータソースの調査結果。3つの領域に分類。

---

### エリア1: マンハッタン需要代理変数 (歩行者流動推定の追加ソース)

既存: MTA Subway Ridership, NYC Pedestrian Counts, NYC TLC Taxi Data

#### 1-1. Citi Bike Trip Data

| 項目 | 内容 |
|------|------|
| 正式名称 | Citi Bike System Data |
| 提供元 | Lyft (Motivate / Citi Bike NYC) |
| URL (公式) | https://citibikenyc.com/system-data |
| URL (NYC Open Data) | https://data.cityofnewyork.us/dataset/Citi-Bike-System-Data/vsnr-94wk |
| 内容 | 個別トリップデータ: 開始/終了ステーション、開始/終了時刻、所要時間、会員種別。スタッフトリップ・60秒未満トリップは除外済 |
| 粒度 | トリップ単位 (ステーション × 時刻) |
| 時間範囲 | 2013年〜現在 (月次ファイル) |
| ファイル形式 | CSV (ZIP圧縮、月100万超は複数CSV) |
| ライセンス | 独自ライセンス (Bikeshare Data License Agreement) |
| 再配布可否 | **制限あり**: スタンドアロンデータセットとしての再配布不可。分析・レポート・研究への組込は非商用に限り可 |
| 用途 | テーマ2: ステーション別発着回数を自転車流動の代理変数として使用。マンハッタンのステーション密度が高い |
| 備考 | データライセンス: https://citibikenyc.com/data-sharing-policy 。Kaggle Dataset同梱不可→notebook内で取得手順を記載する方式 |

#### 1-2. MTA Bus Hourly Ridership

| 項目 | 内容 |
|------|------|
| 正式名称 | MTA Bus Hourly Ridership: 2020-2024 / Beginning 2025 |
| 提供元 | MTA (Metropolitan Transportation Authority) |
| URL (2020-2024) | https://data.ny.gov/Transportation/MTA-Bus-Hourly-Ridership-2020-2024/kv7t-n8in |
| URL (2025〜) | https://data.ny.gov/Transportation/MTA-Bus-Hourly-Ridership-Beginning-2025/gxb3-akrn |
| 内容 | バス路線別・時間帯別の乗客数推計。運賃支払区分別 |
| 粒度 | バス路線 × 1時間 × 運賃区分 |
| 時間範囲 | 2020年〜現在 |
| ファイル形式 | CSV (Open Data NY API対応) |
| ライセンス | パブリック (NY State Open Data、制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: マンハッタン内バス路線の乗客数で地上レベルの移動需要を推定。地下鉄リーチ外エリアの補完 |
| 備考 | 停留所レベルではなく路線レベルの集計。MTA Daily Ridership Data (https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew) は日次システム全体集計で粒度不足 |

#### 1-3. NYC 311 Service Requests

| 項目 | 内容 |
|------|------|
| 正式名称 | 311 Service Requests from 2020 to Present |
| 提供元 | NYC 311 / NYC Open Data |
| URL | https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9 |
| 内容 | 市民からの苦情・要望 (騒音、街灯故障、清掃等)。位置情報 (緯度経度、住所)、日時、カテゴリ含む |
| 粒度 | リクエスト単位 (位置 × 日時 × カテゴリ) |
| 時間範囲 | 2020年〜現在 (日次更新)。2010-2019年データは別データセットあり |
| ファイル形式 | CSV, JSON (SODA API対応) |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: 311リクエスト密度を居住活動・商業活動の間接的プロキシとして使用。騒音苦情は夜間活動強度の指標になりうる |
| 備考 | 2400万行超。全データダウンロードはサイズ大。フィルタリング or API推奨。直接的な歩行者数指標ではないため、補助的な使用に限定 |

#### 1-4. NYC Wi-Fi Hotspot Locations

| 項目 | 内容 |
|------|------|
| 正式名称 | NYC Wi-Fi Hotspot Locations |
| 提供元 | NYC DoITT / NYC Open Data |
| URL | https://data.cityofnewyork.us/Social-Services/NYC-Wi-Fi-Hotspot-Locations/a9we-mtpn |
| 内容 | 公共WiFiホットスポットの位置、プロバイダ名、SSID、設置タイプ |
| 粒度 | ホットスポット単位 (ポイント) |
| 時間範囲 | スナップショット (定期更新) |
| ファイル形式 | CSV, JSON |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: WiFi密度を都市インフラ充実度の代理変数として使用。立地の利便性指標 |
| 備考 | 位置情報のみ (利用量データなし)。立地特徴量の一つとして使用 |

#### 1-5. LinkNYC Kiosk Locations & Usage Statistics

| 項目 | 内容 |
|------|------|
| 正式名称 | LinkNYC Kiosk Locations / LinkNYC Usage Statistics / LinkNYC Weekly Usage (Updated) |
| 提供元 | NYC DoITT / CityBridge, LLC |
| URL (Kiosk Locations) | https://data.cityofnewyork.us/Social-Services/LinkNYC-Kiosk-Locations/s4kf-3yrf |
| URL (Usage - Historical) | https://data.cityofnewyork.us/City-Government/LinkNYC-Usage-Statistics/69wu-b929 |
| URL (Usage - Weekly Updated) | https://data.cityofnewyork.us/City-Government/LinkNYC-Weekly-Usage-Updated-/nxmt-wszr |
| 内容 | キオスク位置・ステータス (Locations)。利用統計: ユーザ数、WiFiセッション数、データ送受信量 (Usage) |
| 粒度 | キオスク単位 × 週次 (Usage) |
| 時間範囲 | 要確認 (Usage Statisticsは複数年蓄積) |
| ファイル形式 | CSV, JSON |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: キオスク利用量 (WiFiセッション数) を歩行者活動の代理変数として使用。キオスクは歩道上に設置されており、利用量は歩行者密度と相関する可能性が高い |
| 備考 | マンハッタン内のキオスク密度は高い。位置+利用量の両方が取得可能な貴重なデータソース |

#### 1-6. NYC Sidewalk Cafe Licenses

| 項目 | 内容 |
|------|------|
| 正式名称 | Sidewalk Café Licenses and Applications |
| 提供元 | NYC Department of Consumer and Worker Protection (DCWP) |
| URL | https://data.cityofnewyork.us/Business/Sidewalk-Caf-Licenses-and-Applications/qcdj-rwhu |
| 内容 | サイドウォークカフェの許可・申請情報。店舗名、住所、許可ステータス |
| 粒度 | 許可申請単位 (位置 + 時点) |
| 時間範囲 | 要確認 |
| ファイル形式 | CSV, JSON |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: サイドウォークカフェの密度を商業活性度・飲食需要の代理変数として使用 |
| 備考 | 2024年に規制改正あり (Dining Out NYC)。位置情報でマンハッタン内をフィルタ可能 |

#### 1-7. NYC Film Permits

| 項目 | 内容 |
|------|------|
| 正式名称 | Film Permits |
| 提供元 | Mayor's Office of Media and Entertainment (MOME) |
| URL | https://data.cityofnewyork.us/City-Government/Film-Permits/tg4x-b46p |
| 内容 | 撮影許可データ。撮影場所 (通り名・ボロー)、日時、カテゴリ (映画/TV/CM等) |
| 粒度 | 許可単位 (通り × 日付) |
| 時間範囲 | 複数年蓄積 |
| ファイル形式 | CSV, JSON |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: 撮影許可の地理的集中度を商業・文化活動の代理変数として使用 |
| 備考 | 5日以上の道路影響があるものに限定される場合あり。補助的な特徴量として位置づけ |

#### 1-8. NYC Permitted Event Information

| 項目 | 内容 |
|------|------|
| 正式名称 | NYC Permitted Event Information |
| 提供元 | NYC Street Activity Permit Office (SAPO) |
| URL | https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information/tvpp-9vvx |
| 内容 | 許可済イベント情報。ストリートフェスティバル、ブロックパーティ、ファーマーズマーケット、プレスカンファレンス等 |
| 粒度 | イベント単位 (位置 × 日付) |
| 時間範囲 | 翌月分の許可済イベント (+ Historical版あり) |
| ファイル形式 | CSV, JSON |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: イベント開催密度を集客力・エリア活性度の代理変数として使用 |
| 備考 | Historical版: https://catalog.data.gov/dataset/nyc-permitted-event-information-historical |

#### 1-9. NYC Pedestrian Mobility Plan — Pedestrian Demand Map

| 項目 | 内容 |
|------|------|
| 正式名称 | Pedestrian Mobility Plan Pedestrian Demand Map / Pedestrian Demand |
| 提供元 | NYC DOT |
| URL (Demand Map) | https://data.cityofnewyork.us/Transportation/Pedestrian-Mobility-Plan-Pedestrian-Demand-Map/c4kr-96ik |
| URL (Demand Data) | https://data.cityofnewyork.us/Transportation/Pedestrian-Mobility-Plan-Pedestrian-Demand/fwpa-qxaf |
| 内容 | 歩行者需要のデータ駆動フレームワーク。Citywide Mobility Surveyに基づく歩行者発生源データ |
| 粒度 | 要確認 (通り or セグメント単位) |
| 時間範囲 | 要確認 |
| ファイル形式 | CSV, JSON, Shapefile |
| ライセンス | NYC Open Data (制限なし) |
| 再配布可否 | 可 |
| 用途 | テーマ2: NYC DOTによる歩行者需要指数。既存のBi-Annual Pedestrian Countsよりカバレッジが広い可能性 |
| 備考 | 既存棚卸し表の4-Aと併用。DOTの公式歩行者需要モデル出力であり、信頼性が高い |

---

### エリア2: Starbucks NLPテキストデータ (10-K / Annual Report以外)

既存: SEC EDGAR 10-K, Starbucks Annual Report PDF

#### 2-1. SEC EDGAR 8-K Filings (Current Reports)

| 項目 | 内容 |
|------|------|
| 正式名称 | SEC EDGAR — Starbucks Corporation 8-K (Current Reports) |
| 提供元 | U.S. Securities and Exchange Commission (SEC) |
| URL (EDGAR検索) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000829224&type=8-K&dateb=&owner=include&count=40 |
| CIK番号 | 0000829224 |
| 内容 | 臨時報告書。決算発表 (earnings release)、経営陣交代、M&A、リストラ等の重要イベント |
| 粒度 | イベント単位 (不定期) |
| 時間範囲 | 1993年〜現在 |
| ファイル形式 | HTML, XBRL |
| ライセンス | パブリックドメイン (米国政府データ) |
| 再配布可否 | 可 |
| 用途 | テーマ1 NLP: 経営戦略転換点のイベント駆動テキスト分析。10-Kの年次テキストを補完する高頻度テキストソース |
| 備考 | 2025年9月のリストラ計画発表 (627店閉鎖) 等、戦略転換の重要テキストを含む |

#### 2-2. SEC EDGAR DEF 14A (Definitive Proxy Statements)

| 項目 | 内容 |
|------|------|
| 正式名称 | SEC EDGAR — Starbucks Corporation DEF 14A (Proxy Statement) |
| 提供元 | SEC |
| URL (EDGAR検索) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000829224&type=DEF+14A&dateb=&owner=include&count=40 |
| 内容 | 株主総会議案書。経営陣報酬、取締役選任、ガバナンス方針、株主提案 |
| 粒度 | 会計年度 (年次) |
| 時間範囲 | 1993年〜現在 |
| ファイル形式 | HTML |
| ライセンス | パブリックドメイン |
| 再配布可否 | 可 |
| 用途 | テーマ1 NLP: ESG関連言語・ガバナンス方針の時系列変化分析。10-Kの事業記述とは異なる経営姿勢テキスト |
| 備考 | NLP分析の優先度は10-K > 8-K > DEF 14A |

#### 2-3. SEC EDGAR Full-Text Search (EFTS)

| 項目 | 内容 |
|------|------|
| 正式名称 | EDGAR Full-Text Search System (EFTS) |
| 提供元 | SEC |
| URL (Web UI) | https://efts.sec.gov/LATEST/search-index?q=%22starbucks%22&forms=10-K,8-K,DEF+14A |
| URL (API docs) | https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| URL (EFTS FAQ) | https://www.sec.gov/edgar/search/efts-faq.html |
| 内容 | 2001年以降の全EDGAR提出書類のフルテキスト検索。添付資料 (Exhibit) も検索対象 |
| 粒度 | 書類単位 |
| 時間範囲 | 2001年〜現在 |
| ファイル形式 | JSON (API応答) |
| ライセンス | パブリックドメイン |
| 再配布可否 | 可 |
| 用途 | テーマ1 NLP: Starbucks関連の全SEC提出書類を網羅的に発見・取得するための検索基盤 |
| 備考 | Bulk download用: companyfacts.zip (XBRL)、submissions.zip (提出履歴)。User-Agentヘッダ要 |

#### 2-4. Earnings Call Transcripts

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Earnings Call Transcripts |
| 提供元 (候補1) | The Motley Fool |
| URL (候補1) | https://www.fool.com/earnings-call-transcripts/ (SBUX検索) |
| 提供元 (候補2) | Seeking Alpha |
| URL (候補2) | https://seekingalpha.com/symbol/SBUX/earnings/transcripts |
| 内容 | 四半期決算発表後の経営陣によるアナリスト向け電話会議の全文書起こし。CEO/CFOの冒頭説明 + Q&Aセッション |
| 粒度 | 四半期 (年4回) |
| 時間範囲 | 要確認 (Motley Foolは近年の主要企業をカバー) |
| ファイル形式 | HTML (Web閲覧) |
| ライセンス | **著作権あり (各プラットフォーム)** |
| 再配布可否 | **不可**。Seeking Alphaは個人・非商用閲覧のみ、複製・再配布・派生物作成を明示的に禁止。Motley Foolも同等の制限と推定 |
| 用途 | テーマ1 NLP: 経営言語の四半期変化分析。10-K (年次) より高頻度で経営陣の生の言葉を含む |
| 備考 | **notebook内で取得手順のみ記載、データ同梱不可**。分析結果 (トピック分布等) のみ公開。代替として8-K内のearnings release (Press Release as Exhibit) を使えばパブリックドメインで類似分析が可能 |

#### 2-5. Starbucks Press Releases / Newsroom

| 項目 | 内容 |
|------|------|
| 正式名称 | Starbucks Press Releases / Starbucks Stories |
| 提供元 | Starbucks Corporation |
| URL (Press Releases) | https://about.starbucks.com/press/press-releases/ |
| URL (Stories/News) | https://about.starbucks.com/stories/category/news/ |
| URL (IR Press) | https://investor.starbucks.com/news/financial-releases/ |
| 内容 | 公式プレスリリース: 新製品発表、パートナーシップ、ESG活動、財務リリース等 |
| 粒度 | リリース単位 (不定期) |
| 時間範囲 | 要確認 (直近数年分は確実にアクセス可能) |
| ファイル形式 | HTML (Web) |
| ライセンス | 著作権はStarbucks社 |
| 再配布可否 | 不可 (フェアユース範囲での分析引用は可) |
| 用途 | テーマ1 NLP: ブランドメッセージング・戦略コミュニケーションの時系列分析 |
| 備考 | SEC EDGAR 8-Kの方がパブリックドメインで取り扱いやすい。Starbucks Newsroomは補完的位置づけ |

---

### エリア3: 競合コーヒーチェーン店舗位置データ

既存: OSM (amenity=cafe) — ブランド別の具体的調査が未実施

#### 3-1. OpenStreetMap — ブランドタグによるチェーン別クエリ

| 項目 | 内容 |
|------|------|
| 正式名称 | OpenStreetMap Brand Tag Queries (Overpass API) |
| 提供元 | OpenStreetMap Contributors |
| URL (Overpass Turbo) | https://overpass-turbo.eu/ |
| 内容 | `brand=*` タグでコーヒーチェーンを個別抽出。Dunkin', Peet's Coffee, Blue Bottle Coffee, Tim Hortons, Gregory's Coffee等 |
| クエリ例 | `node["brand"="Dunkin'"](40.70,-74.02,40.88,-73.90); out;` (マンハッタン bbox) |
| 粒度 | POI (ノード) 単位 |
| ファイル形式 | JSON, CSV (Overpass Turbo export) |
| ライセンス | ODbL 1.0 |
| 再配布可否 | 可 (ODbL準拠: 出典表記 + 派生DB同一ライセンス) |
| 用途 | テーマ2: マンハッタン内の主要競合チェーン位置を取得。既存棚卸し表10-Aのクエリを具体化 |
| 備考 | マンハッタンはOSMカバレッジが高く、チェーン店はbrandタグが比較的整備されている。ただし網羅性は保証されないため、取得後に公式店舗数と照合して補完率を確認すべき |

#### 3-2. Kaggle — USA Dunkin' Donuts Stores

| 項目 | 内容 |
|------|------|
| 正式名称 | USA Dunkin Donuts Stores |
| 提供元 | jpbulman (Kaggleユーザ) |
| URL | https://www.kaggle.com/datasets/jpbulman/usa-dunkin-donuts-stores |
| 内容 | 全米のDunkin'店舗位置。住所、座標 (緯度経度) |
| 粒度 | 店舗単位 |
| 時間範囲 | 要確認 (スナップショット) |
| ファイル形式 | CSV |
| ライセンス | 要確認 (Kaggleページで確認要) |
| 再配布可否 | 要確認 |
| 用途 | テーマ2: Starbucks最大の競合であるDunkin'のマンハッタン店舗を抽出し、空間的競合分析に使用 |
| 備考 | 別のKaggleデータセットも存在: https://www.kaggle.com/datasets/appleturnovers/dunkin-locations 。data.worldにも類似データあり: https://data.world/nkumtakar/dunkin-donuts |

#### 3-3. ScrapeHero Data Store — コーヒーチェーン位置データ (参考情報)

| 項目 | 内容 |
|------|------|
| 正式名称 | ScrapeHero Location Datasets (Peet's Coffee / Blue Bottle / Tim Hortons / Dunkin') |
| 提供元 | ScrapeHero |
| URL (参考) | https://www.scrapehero.com/store/ |
| 内容 | 各チェーンのジオコード付き店舗位置。住所、電話番号、営業時間 |
| 粒度 | 店舗単位 |
| 時間範囲 | 週次更新 |
| ファイル形式 | Excel, CSV (JSON/GeoJSON/KML は追加費用) |
| ライセンス | 商用ライセンス |
| 再配布可否 | 不可 (商用データ) |
| 用途 | — |
| 備考 | **このプロジェクトでは使用不可** (有料・再配布不可)。OSMまたはKaggleデータで代替する。Peet's: 286店、Blue Bottle: 78店、Tim Hortons: 689店 (2025年時点の概数として参考) |

#### 3-4. Yelp Open Dataset

| 項目 | 内容 |
|------|------|
| 正式名称 | Yelp Open Dataset |
| 提供元 | Yelp Inc. |
| URL | https://business.yelp.com/data/resources/open-dataset/ |
| URL (Kaggle mirror) | https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset |
| 内容 | ビジネス情報 (business.json): 店舗名、カテゴリ、座標、属性、星評価。レビュー (review.json)、チェックイン (checkin.json) 等6ファイル。約160,000ビジネス、860万レビュー |
| 粒度 | ビジネス単位 / レビュー単位 |
| 時間範囲 | 要確認 (定期更新) |
| ファイル形式 | JSON |
| ライセンス | Yelp Dataset License (academic / educational use限定) |
| 再配布可否 | **不可** (教育・学術目的の個人使用のみ) |
| 用途 | テーマ2: マンハッタンが対象都市に含まれている場合、カフェカテゴリのビジネスを競合データとして使用可能。レビューテキストのNLP分析も可能性あり |
| 備考 | **重大な制約**: (1) 対象都市がマンハッタンを含むか要確認 (限定された都市のサブセット)。(2) データセット同梱不可→notebook内で取得手順のみ記載。(3) Kaggle上のmirrorは2024年4月版あり。ライセンス条件をダウンロード時に要確認 |

---

### エリア別 推奨度サマリー

#### エリア1: マンハッタン需要代理変数 — 推奨度

| データソース | 推奨度 | 理由 |
|---|---|---|
| MTA Bus Hourly Ridership (1-2) | **★★★ 高** | パブリック、路線レベル時間帯別、地下鉄補完 |
| LinkNYC Usage Statistics (1-5) | **★★★ 高** | パブリック、位置+利用量のユニークな組合せ |
| Citi Bike Trip Data (1-1) | **★★☆ 中** | 高品質だが再配布制限あり→notebook手順記載方式 |
| NYC Pedestrian Demand Map (1-9) | **★★☆ 中** | DOT公式モデル出力、既存歩行者データと併用 |
| NYC 311 Service Requests (1-3) | **★☆☆ 低** | 間接的プロキシ、データ量大、コスパ低 |
| Sidewalk Cafe Licenses (1-6) | **★☆☆ 低** | 商業活性度の静的指標としてのみ有用 |
| Film Permits (1-7) | **★☆☆ 低** | 補助的。撮影=歩行者需要とは限らない |
| Event Permits (1-8) | **★☆☆ 低** | 補助的。イベント期間のみの効果 |
| WiFi Hotspot Locations (1-4) | **★☆☆ 低** | 位置のみ (利用量なし)、LinkNYCで代替 |

#### エリア2: NLPテキストデータ — 推奨度

| データソース | 推奨度 | 理由 |
|---|---|---|
| SEC EDGAR 8-K (2-1) | **★★★ 高** | パブリックドメイン、高頻度テキスト、戦略転換点 |
| EFTS全文検索 (2-3) | **★★★ 高** | 網羅的発見ツール、APIアクセス可 |
| DEF 14A Proxy (2-2) | **★★☆ 中** | パブリックドメイン、ガバナンス分析に有用 |
| Earnings Transcripts (2-4) | **★★☆ 中** | 高品質テキストだが再配布不可。8-K Exhibitで部分代替可 |
| Starbucks Newsroom (2-5) | **★☆☆ 低** | 著作権あり、8-K press releaseと重複多い |

#### エリア3: 競合コーヒーチェーン — 推奨度

| データソース | 推奨度 | 理由 |
|---|---|---|
| OSM Brand Queries (3-1) | **★★★ 高** | ODbL、マンハッタン高カバレッジ、複数チェーン一括取得 |
| Kaggle Dunkin' (3-2) | **★★☆ 中** | ライセンス要確認、OSM補完用 |
| Yelp Open Dataset (3-4) | **★☆☆ 低** | マンハッタン含むか不明、再配布不可 |
| ScrapeHero (3-3) | **☆☆☆ 不可** | 有料・再配布不可、プロジェクト制約に抵触 |

---

### ライセンス・再配布の追加サマリー

| データソース | ライセンス | 再配布 | Kaggle Dataset同梱 |
|---|---|---|---|
| Citi Bike Trip Data | Bikeshare独自ライセンス | **制限あり** (スタンドアロン不可、非商用分析への組込のみ可) | **不可**→取得手順のみ |
| MTA Bus Hourly Ridership | パブリック (NY State Open Data) | 可 | 可 |
| NYC 311 Service Requests | NYC Open Data (制限なし) | 可 | 可 (サイズ注意) |
| NYC WiFi Hotspot Locations | NYC Open Data (制限なし) | 可 | 可 |
| LinkNYC Locations / Usage | NYC Open Data (制限なし) | 可 | 可 |
| Sidewalk Cafe Licenses | NYC Open Data (制限なし) | 可 | 可 |
| Film Permits | NYC Open Data (制限なし) | 可 | 可 |
| Event Permits | NYC Open Data (制限なし) | 可 | 可 |
| Pedestrian Demand Map | NYC Open Data (制限なし) | 可 | 可 |
| SEC EDGAR 8-K / DEF 14A / EFTS | パブリックドメイン | 可 | 可 |
| Earnings Transcripts (Motley Fool / SA) | 著作権あり (各社) | **不可** | **不可**→取得手順のみ |
| Starbucks Newsroom | 著作権あり (Starbucks社) | 不可 | 不可→取得手順のみ |
| OSM Brand Queries | ODbL 1.0 | 可 (帰属表示+同一ライセンス) | 可 (ODbL条件遵守) |
| Kaggle Dunkin' | 要確認 | 要確認 | 要確認 |
| Yelp Open Dataset | 教育・学術限定 | **不可** | **不可**→取得手順のみ |

---

### テーマ別データマッピング (更新版)

#### テーマ1: 全米30年空間アニメーション + NLP (追加分のみ)

| 分析要素 | 追加データソース | 優先度 |
|---|---|---|
| NLPテキスト (高頻度) | SEC EDGAR 8-K | 高 |
| NLPテキスト (ガバナンス) | SEC EDGAR DEF 14A | 中 |
| NLPテキスト (四半期) | Earnings Call Transcripts (再配布不可) | 中 |
| テキスト網羅的検索 | EDGAR EFTS | 高 |

#### テーマ2: マンハッタンドミナント戦略分析 (追加分のみ)

| 分析要素 | 追加データソース | 優先度 |
|---|---|---|
| 自転車流動 | Citi Bike Trip Data | 中 |
| バス乗客 | MTA Bus Hourly Ridership | 高 |
| キオスク利用量 | LinkNYC Usage Statistics | 高 |
| 歩行者需要モデル | NYC Pedestrian Demand Map | 中 |
| 商業活性度 | Sidewalk Cafe Licenses | 低 |
| 競合チェーン位置 | OSM Brand Queries (Dunkin', Peet's, Blue Bottle, Tim Hortons) | 高 |
| 競合チェーン位置 (補完) | Kaggle Dunkin' Stores | 中 |

---

## 次のアクション (TODO)

- [ ] Kaggle Starbucks公式データセットのライセンスをダウンロードページで確認
- [ ] Kaggle 2023版のライセンス・カラム構成を確認
- [ ] SEC EDGAR XBRL Company Facts APIで店舗数データの取得テスト
- [ ] NYC Bi-Annual Pedestrian Countsのマンハッタン内地点数・時間範囲を確認
- [ ] MTA Subway Hourly Ridership APIの駅一覧・マンハッタン対応を確認
- [ ] MapPLUTO最新版のダウンロードとカラム確認
- [ ] Overpass APIでマンハッタン内 amenity=cafe のPOI数とカバレッジを確認
- [ ] NYC TLCデータのマンハッタンTaxi Zone IDマッピングを確認
- [ ] BLS QCEW New York County (FIPS 36061) のダウンロードテスト
- [ ] **Overpass APIでマンハッタン内のbrand別コーヒーチェーン (Dunkin', Peet's, Blue Bottle, Tim Hortons, Gregory's) のPOI数を確認**
- [ ] **MTA Bus Hourly Ridership APIからマンハッタン内路線を抽出しサンプルデータ確認**
- [ ] **LinkNYC Usage Statistics のカラム構成・マンハッタン内キオスク数を確認**
- [ ] **Citi Bike Trip Dataのマンハッタン内ステーション数・データサイズを確認**
- [ ] **SEC EDGAR 8-K filing一覧をStarbucks CIK=0000829224で取得し件数・時間範囲を確認**
- [ ] **NYC Pedestrian Demand Map/Demandデータのカラム構成・粒度を確認**
- [ ] **Kaggle Dunkin'データセットのライセンス・カラム・レコード数を確認**
- [ ] **Yelp Open Datasetの対象都市にNYCが含まれるか確認**
