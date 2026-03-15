# データ棚卸し結果サマリー

最終更新: 2026-03-12

---

## テーマ1で使うデータソース

### Sランク（コア。これがないと分析が成立しない）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| SEC EDGAR 10-K | NLPテキスト + 店舗数時系列 | 可 | 可 |
| TIGER/Line Shapefiles | 全米ベースマップ（州・郡境界） | 可 | 可 |

### Aランク（強く使いたい。再配布可能）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| US Census ACS 5-Year | ZIP/County別人口で出店密度を正規化 | 可 | 可 |
| SEC EDGAR 8-K | 四半期決算リリース。NLPテキスト補完 | 可 | 可 |

### Bランク（あると良いが代替可能 or 再配布不可）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| Kaggle Starbucks Locations (1-A) | 店舗地理位置のスナップショット | グレー | 手順のみ |
| Starbucks Annual Report PDF | NLP補完資料 | 不可 | 手順のみ |
| ACS 1-Year | 時系列の経年比較 | 可 | 可 |

### 使わない（Cランク）

| データソース | 理由 |
|---|---|
| Kaggle 2023版 (1-B) | ライセンス誤設定（Reddit API Terms）。信頼性に問題 |
| Kaggle 2021版 (1-C) | ライセンス未確認。1-Aで十分 |
| Earnings Call Transcripts | 再配布不可（Seeking Alpha/Motley Fool規約） |

---

## テーマ2で使うデータソース

### Sランク（コア）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| OSM brand=Starbucks | マンハッタンStarbucks店舗位置（171店舗） | 可（ODbL） | 可 |
| OSM amenity=cafe | 競合カフェ位置（1,220件、Dunkin' 115含む） | 可（ODbL） | 可 |
| MapPLUTO | ビル属性・用途・容積率・建築年（42,600区画） | 可 | 可 |
| OSM道路ネットワーク (via OSMnx) | 歩行距離・ネットワーク分析 | 可（ODbL） | 可 |

### Aランク（強く使いたい）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| MTA Subway Hourly Ridership | 駅別時間帯別乗降客数（161駅） | 可 | 可 |
| NYC Bi-Annual Pedestrian Counts | 歩行者カウント（マンハッタン36地点、2007-2025） | 可 | 可 |
| US Census ACS 5-Year | Census Tract別の所得・人口 | 可 | 可 |
| TIGER/Line (Census Tract) | マンハッタンCensus Tractポリゴン | 可 | 可 |

### Bランク（あると良いが代替可能）

| データソース | 用途 | 再配布 | 同梱 |
|---|---|---|---|
| NYC TLC Trip Data | Taxi Zone別乗降数で地域活性度推定 | 可 | 可（サイズ注意） |
| BLS QCEW | オフィスワーカー密度推定 | 可 | 可 |
| Building Footprints | ビル外周ポリゴン。PLUTOとBBLでジョイン | 可 | 可 |
| MTA Bus Hourly Ridership | バス路線別乗降で地下鉄を補完 | 可 | 可 |
| LinkNYC Usage Statistics | キオスクWiFiセッション数 | 可 | 可 |

### 使わない（Cランク）

| データソース | 理由 |
|---|---|
| Citi Bike Trip Data | 再配布不可（Bikeshare License） |
| Yelp Open Dataset | 学術利用のみ、NYC含まれるか不明 |
| Foursquare/Kaggle POI | ライセンス個別確認が必要。OSMで十分 |
| NYC 311 / Film Permits / Event Permits | 間接的すぎる。工数に見合わない |

---

## 最大のリスク

1. **Starbucks店舗の開店年データが存在しない**
   - Kaggleデータはスナップショットのみ（2017/2021/2023時点）
   - テーマ1の「30年の空間的増殖アニメーション」は、10-Kから年次店舗数を取得し、Kaggleスナップショットの差分で推定する必要あり
   - 最悪、年次の「店舗数推移グラフ」+「特定時点の地図」の組み合わせに縮小

2. **歩行者カウントの地点数が限定的**
   - マンハッタン内36地点のみ。店舗171に対してカバレッジが粗い
   - MTA駅乗降データ（161駅）で補完可能。組み合わせれば実用レベル

3. **OSM Starbucks店舗数とKaggleの差異**
   - OSM: 171店舗 vs 実際: 約200店舗（約85%カバー）
   - 欠落店舗の傾向を確認する必要あり（ビル内店舗が漏れやすい等）

---

## 歩行者データの実現可能性（暫定判断）

**実現可能**。以下の3層構造で需要代理変数を構築する。

| 層 | データソース | 粒度 | カバレッジ |
|---|---|---|---|
| 1（直接計測） | NYC Pedestrian Counts | 36地点 | 低い。小売コリドー限定 |
| 2（駅乗降） | MTA Subway Hourly Ridership | 161駅 | 高い。マンハッタンほぼ網羅 |
| 3（車両需要） | NYC TLC Trip Data | Taxi Zone | 高い。乗降パターンで地域活性度推定 |

3層を組み合わせることで、マンハッタン全域の人流推定は十分に可能。

---

## 次のステップ

1. **名寄せ設計** — OSM店舗データとMapPLUTOのBBL/住所をどう結合するかの設計
2. **MapPLUTO全量ダウンロード** — API経由で42,600区画を一括取得
3. **SEC EDGAR 10-Kテキスト取得テスト** — 最初の1ファイルをダウンロードしてNLP前処理のプロトタイプ作成
4. **OSMデータの欠落検証** — Kaggle店舗データとOSMの差分を確認し、欠落パターンを把握
