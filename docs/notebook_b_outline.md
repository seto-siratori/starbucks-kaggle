# Notebook B 構成設計

作成日: 2026-03-13

---

## 設計原則

- **Notebook Aの「WHERE」から Notebook Bの「WHY / WHAT IF」へ**
- Notebook A: 店舗がどこにクラスターしているか（記述的分析）
- Notebook B: どのエリアが供給過剰/不足で、次にどこに出店すべきか（予測的分析）
- 15-25分で読める。Notebook Aを読まなくても単体で成立する設計
- 再現可能テンプレート: 読者が自分の都市・ブランドに転用できる構造を維持

---

## 核となる問い

> **「マンハッタンの309 Census Tractのうち、どこがスタバの供給過剰（over-served）で、どこが供給不足（under-served）か？」**

これを「立地適応度スコア（Location Fitness Score）」で定量化する。

---

## タイトル案

1. **"Where Should the 172nd Starbucks Go? A Location Fitness Model for Manhattan"**
   - 具体的な数字＋疑問形 → クリック率が高い
2. **"Over-Served or Under-Served? Demand vs Supply Scoring for 309 Census Tracts"**
   - 分析手法が明確。ビジネスアナリスト向け
3. **"Location Fitness Score: Predicting Starbucks Gaps with Transit, Population & Competition Data"**
   - テンプレート性が伝わる
4. **"Starbucks Location Intelligence: Demand-Supply Gap Analysis in Manhattan (Reusable Template)"**
   - Notebook Aとのシリーズ感＋テンプレート訴求

### 決定

> **"Where Should the 172nd Starbucks Go? Demand-Supply Gap Scoring for Manhattan (Reusable Template)"**

理由:
- 「172nd」→ 既に171店があることを暗示し、Notebook Aとの連続性を示す
- **疑問形** → 答えが気になって読み進める構造
- **「Reusable Template」** → Notebook Aと統一感

---

## 立地適応度スコアの設計

### 基本構造

```
Location Fitness Score (LFS) = Demand Proxy Index / Supply Density
```

- **LFS > 1**: 需要に対して供給が少ない → **under-served（出店候補）**
- **LFS < 1**: 需要に対して供給が多い → **over-served（カニバリゼーションリスク）**
- **LFS ≈ 1**: 均衡状態

### 需要代理変数（Demand Proxy）

Census Tract単位で以下を正規化（0-1スケール）して重み付き合成:

| 変数 | ソース | 論拠 | 重み候補 |
|---|---|---|---|
| MTA乗降客数（最寄り駅） | MTA Hourly Ridership | Notebook Aで r=0.58 を確認済み。最強の需要代理 | **0.40** |
| 歩行者通行量 | NYC Bi-Annual Pedestrian Counts | 駅以外の人流。114地点→Tract空間結合 | **0.25** |
| 昼間就業人口密度 | ACS通勤者データ + PLUTO comarea | オフィス街の昼間需要 | **0.20** |
| 居住人口密度 | ACS tract_population / ALAND | 住宅街の朝晩需要 | **0.15** |

**重みの決め方**: 初期値は上記で固定し、感度分析（Section 4）で重みを変えた場合にランキングがどう変わるかを示す。重みの「正解」は売上データがない限り不明であることを明記する。

**採用しない変数と理由**:
- **世帯所得**: Notebook Aで r=0.03（無相関）を確認済み。需要代理として不適格
- **学歴**: 所得と同様、立地選択との直接的関連が弱い

### 供給密度（Supply Density）

| 変数 | 計算方法 |
|---|---|
| Tract内スタバ数 | stores_enriched_v3 → groupby tract |
| Tract内全カフェ数 | manhattan_cafes_osm → sjoin tract |
| 500m圏内競合密度（平均） | 既存カラム: n_other_cafe_500m の tract平均 |

供給変数は「Tract内スタバ + 0.5 × Tract内その他カフェ」で合成。スタバ同士のカニバリゼーションを重く、異ブランド競合を軽く扱う。

### 0店舗Tractの扱い

309 Tractのうち205にスタバがない。供給=0のTractはLFSが無限大になるため:
- 供給変数に floor = 0.1 を設定（「0店舗でも最小供給量を仮定」）
- ただし需要代理も低い（住宅専用地や公園）Tractは自動的にLFSが低くなるので、ランキング上位には来ない

---

## セクション構成

### Section 0: Setup & Data Loading (3 cells)

- pip install + imports（Notebook Aと同じ自動検出パス）
- stores_enriched_v3.csv + manhattan_cafes_osm.csv + manhattan_tracts_lisa.geojson 読み込み
- 歩行者カウントデータの読み込み（Dataset v3に同梱 or notebook内でフェッチ）

**使うデータ**: manhattan-cafe-wars Dataset (v2/v3)

---

### Section 1: The Hook — The Map of Gaps (3 cells)

**図1**: 309 Tract choropleth map — 色=スタバ数（0, 1, 2, 3+）

> *「マンハッタンの309 Census Tractのうち、205（66%）にスタバは1店舗もない。残る104 Tractに171店が集中している。しかし『スタバがないTract = 出店機会』ではない。需要がなければ出店しない。問題は、需要があるのにスタバがないTractがあるかどうかだ。」*

**図2**: 2軸散布図 — x=需要代理スコア、y=供給密度、色=LISA cluster
- 右下のゾーン（需要高×供給低）が出店候補
- Notebook AのLISA結果をここで再利用

**書く結論**: 「需要が高いのにスタバがないTract」が存在するかどうかの第一印象。

**免責表明（Section 1 のマークダウンに必ず含める）**:

> *"Important: The weights used in this scoring model are assumptions based on Notebook A's findings (ridership r=0.58, income r=0.03), not calibrated against actual sales data. Section 4 tests how sensitive the results are to these assumptions."*

この1文をSection 1 の導入マークダウンに入れることで、読者が最初に「これは仮定であり、検証済みの重みではない」と理解した上で読み進める構造にする。Limitationsセクション（Section 7）は最後まで読まれない可能性があるため、免責は冒頭で先に出す。

---

### Section 2: Building the Demand Proxy (4 cells)

**図3**: 4パネルchoropleth — Tract単位の需要代理変数それぞれの分布
- MTA乗降客数（最寄り駅のTract割当て）
- 歩行者通行量（114地点→Tract空間結合→補間）
- 昼間就業人口密度（PLUTO comarea × 業種別就業密度で推定）
- 居住人口密度

**コード**: 各変数をmin-maxスケーリング → 重み付き合成 → Demand Proxy Index (DPI)

**書く結論**: 需要が高いTractは Midtown/FiDi/Chelsea に集中するが、一部のUpper West SideやEast Village Tractも高い。

**テンプレートノート**: 読者は自分の都市の人流データに差し替えるだけで同じDPIが計算できる。

---

### Section 3: Location Fitness Score (4 cells)

**コード**: LFS = DPI / Supply_Normalized

**図4**: 309 Tract choropleth — 色=LFS（赤=over-served、青=under-served、白=均衡）

**図5**: LFS上位10 Tract（under-served）のテーブル + 地図上ハイライト
- Tract名、需要スコア、供給数、LFS値、地理的特徴

**図6**: LFS下位10 Tract（over-served）のテーブル
- 「ここにはスタバが多すぎる」Tract一覧

**書く結論**:
- over-served上位はChelsea/Midtown（予想通り — LISA HH と一致）
- under-served上位に「意外な」Tractがあるか？（例: Upper West Side の一部、East Village のFoot traffic高エリア）

---

### Section 4: Sensitivity Analysis — Do Weights Matter? (3 cells)

重みを変えた3シナリオでランキングがどう変わるか:

| シナリオ | MTA | 歩行者 | 就業人口 | 居住人口 | 想定状況 |
|---|---|---|---|---|---|
| Baseline | 0.40 | 0.25 | 0.20 | 0.15 | バランス型 |
| Transit-Heavy | 0.60 | 0.20 | 0.15 | 0.05 | 通勤者ターゲット |
| Residential | 0.20 | 0.15 | 0.10 | 0.55 | 住宅街ターゲット |

**図7**: 3シナリオの上位10 Tractの比較テーブル（Rank Correlation）

**書く結論**:
- 上位5 Tractが3シナリオで共通なら → ロバストな出店候補
- シナリオで大きく変わるなら → 重み設定が結論を左右する（=売上データなしの限界）

---

### Section 5: Cannibalization Risk — Walk-Distance Overlap (3 cells)

**問い**: 既存スタバ同士の歩行圏（5分=400m）はどのくらい重なっているか？

**方法A（採用）: 直線距離ベースの近似**
- Notebook Aの nearest_starbucks_dist_m を使用
- 400m以内に別のスタバがある店舗 = カニバリゼーションリスクあり
- Tract単位でカニバリ率を計算 → LFSの供給項に追加ペナルティ

**方法B（参考情報として言及のみ）: OSMnxネットワーク距離**
- 171店 × 123駅 = 21,033ペアのネットワーク距離は計算コストが高い
- Kaggle環境でのタイムアウトリスク（1ペアあたり0.5-1秒 × 21K = 3-6時間）
- **Notebookに含めない。** 代わりに「OSMnxを使えば歩行距離ベースの精密なカニバリ分析が可能」とコードスニペットのみ記載

**図8**: 既存171店のカニバリゼーションマップ — 色=400m以内の同ブランド店舗数

**書く結論**: Midtown/Chelseaでは1店舗あたり平均X店が400m圏内に存在。住宅街ではほぼ0。ドミナント戦略が意図的なものか、需要が支えているかはLFSで判断できる。

---

### Section 6: Reusable Template Function (2 cells)

```python
def compute_location_fitness(stores_df, competitors_df, polygon_gdf,
                              demand_proxies, weights, supply_col="store_count"):
    """
    Census Tract（or任意のポリゴン）ごとの立地適応度スコアを計算。

    Parameters:
        demand_proxies: dict of {column_name: weight}
        supply_col: ポリゴンGeoDataFrame内の供給カラム名
    Returns:
        GeoDataFrame with LFS column
    """
```

**テンプレートノート**: 「あなたの都市のデータに差し替えて実行してください」

---

### Section 7: Limitations & What's Next (2 cells)

**制約の明記**:

| 制約 | 影響 | 緩和策 |
|---|---|---|
| 売上データなし | 需要代理の重みが検証不能 | 感度分析で重みへの依存度を明示 |
| 歩行者カウント114地点 | Tract全域をカバーしていない | 最近接地点の値で代替（空間補間の精度は限定的） |
| 静的スナップショット | 出退店の動態を無視 | 時系列分析はテーマ1のスコープ |
| 直線距離 ≠ 歩行距離 | カニバリ分析の精度に限界 | OSMnx使用の手順を記載 |
| Census Tract粒度 | ブロック単位の需要差を無視 | 点レベルのNN分析（Notebook A）で補完 |

**バックテスト構想（将来の拡張として言及のみ）**:
- Kaggle Starbucks directory.csv（2017年時点）と OSM 2026年データの差分で閉店候補を推定
- ただし directory.csv はデータ取得が別途必要。本Notebookではカバーしない
- 閉店店舗がLFS低スコアTractに集中していれば、スコアの妥当性を事後検証できる

**Notebook Aへの導線（逆リンク）**:
> *"This notebook scored Census Tracts by demand-supply balance. For the statistical foundation (Moran's I, Ripley's K, LISA clusters), see Notebook A."*

---

## Notebook A → Notebook B の依存関係

| Notebook B が使うもの | ソース |
|---|---|
| stores_enriched_v3.csv | Dataset v2 に同梱済み |
| manhattan_tracts_lisa.geojson | Dataset v2 に同梱済み |
| manhattan_cafes_osm.csv | Dataset v2 に同梱済み |
| LISA cluster labels | geojson 内のlisa_cluster列。Section 1で再利用 |
| Notebook A の r=0.58 / r=0.03 の知見 | Section 2 の変数選択の根拠として文中で引用 |

**Notebook B が新たに必要とするデータ**:

| データ | 取得方法 | サイズ |
|---|---|---|
| 歩行者カウント（114地点） | NYC Open Data: Bi-Annual Pedestrian Counts | 114行。data/raw に取得済み |
| Census Tract別 昼間人口推計 | ACS B08301 or PLUTO comarea から推計 | 計算で生成 |

---

## セル数見積もり

| Section | コード | マークダウン | 計 |
|---|---|---|---|
| 0: Setup | 2 | 1 | 3 |
| 1: Hook | 2 | 1 | 3 |
| 2: Demand Proxy | 3 | 1 | 4 |
| 3: LFS | 3 | 1 | 4 |
| 4: Sensitivity | 2 | 1 | 3 |
| 5: Cannibalization | 2 | 1 | 3 |
| 6: Template | 1 | 1 | 2 |
| 7: Limitations | 0 | 2 | 2 |
| **合計** | **15** | **9** | **24** |

目標 24 cells、読了 15-20分。Notebook A の 26 cells とほぼ同規模。

---

## バックテスト設計の詳細（実装は将来）

### 目的

LFSスコアが「現実に意味のある指標」であることを事後検証する。

### 手法

1. **2017年時点の店舗リスト**: Kaggle Starbucks directory.csv（全米）からマンハッタンを抽出
2. **2026年時点の店舗リスト**: OSM データ（現在の171店）
3. **差分**: 2017年にあって2026年にない店舗 = 閉店候補
4. **検証**: 閉店候補のTractのLFSスコアの分布と、存続店舗のTractのLFS分布を比較
   - 閉店TractのLFS中央値 < 存続TractのLFS中央値 なら、スコアに予測力がある

### 注意事項

- directory.csv と OSM は座標系・店舗名の表記が異なるため、空間的近接度（50m以内）でマッチング
- 「OSMにない＝閉店」ではなく「OSMに未登録」の可能性もある（OSMカバレッジ85%）
- サンプルサイズが小さい（閉店数が10-20程度と予想）ため、統計的検定力は限定的
- **結論を控えめに書く**: 「LFSスコアと閉店に関連がある示唆が見える」程度

---

## OSMnx歩行圏分析の判断

### 結論: Notebook B には含めない

### 理由

1. **計算コスト**: 171店×123駅 = 21,033ペアのネットワーク距離。OSMnx の shortest_path は1ペア0.5-1秒 → 3-6時間。Kaggleのタイムアウト（9時間）に収まるが余裕がない
2. **グラフのダウンロード**: マンハッタン歩行ネットワークのダウンロードにInternet ON が必要。Kaggle Notebook は Internet ON で実行時間制限がさらに厳しくなる
3. **直線距離との乖離**: マンハッタンのグリッド構造では、直線距離 × 1.4（マンハッタン距離係数）で十分な近似が得られる。ネットワーク距離の精度向上に対するコストが見合わない
4. **代替案**: Section 5 で「直線距離 × √2 で近似」を採用し、OSMnx のコードスニペットを参考情報として記載する

### 将来的な拡張としての位置づけ

- Notebook C（もし作る場合）で OSMnx 歩行圏ポリゴンを使った「徒歩5分圏サービスエリア」分析を実施
- または「OSMnx 歩行距離の計算は重いので、ローカル環境で事前計算し、結果CSVだけをDatasetに含める」方式

---

## Dataset v3 の検討

Notebook B をKaggleで動かすために、Dataset をさらに拡張する可能性:

| 追加候補ファイル | 理由 |
|---|---|
| manhattan_pedestrian_counts.csv | 114地点の歩行者カウント。Notebook内でフェッチも可能だが同梱が確実 |
| tract_demand_supply_scores.csv | LFS計算結果。Notebookが生成するので同梱不要だが、他ユーザーが分析するなら便利 |

→ **最小構成**: 歩行者カウントのみ追加。LFSは Notebook が生成する方が再現性が明確。
