# Notebook Theme 1 構成設計

作成日: 2026-03-13

---

## 設計原則

- **30年間の経営言語の変化と店舗拡大を重ね合わせ、「スタバは何を語りながら成長したか」をデータで可視化する**
- NLP分析（キーワード頻度・LDAトピックモデリング）と店舗数時系列を組み合わせた複合分析
- 10-Kアニュアルレポート30年分を定量テキストマイニングの対象とし、経営戦略の転換点を言語から検出する
- 15-25分で読める。テーマ2（マンハッタン空間分析）を読まなくても単体で成立する設計
- Hero chart（4パネル統合図）を最終成果物とし、1枚で30年のストーリーが伝わる構造

---

## 核となる問い

> **「スターバックスは30年間で何を語り、何を語らなくなったか？ そしてそれは店舗拡大のどの局面と対応するか？」**

10-Kの言語変化と店舗数時系列を重ね合わせ、経営戦略の転換点をテキストデータから検出する。

---

## タイトル案

1. **"30 Years of Starbucks 10-K Filings: NLP Topic Modeling & Keyword Trend Analysis (LDA + SEC EDGAR, Reusable Template)"**
   - 手法名（NLP Topic Modeling, LDA）で検索ヒット、データソース名（SEC EDGAR）で再現性、Reusable Templateで汎用性。テーマ2 Notebook A/Bの命名規則と一貫
2. **"From 1,006 to 40,576: How Starbucks Talked Its Way Through 30 Years of Growth"**
   - 数字のインパクト＋「語り方」という切り口 → 好奇心を引く。リード文やSection 1見出しに活用
3. **"Starbucks Beyond Coffee: NLP Analysis of 30 Years of 10-K Filings"**
   - NLP手法が明確。データサイエンティスト向け

### 決定

> **"30 Years of Starbucks 10-K Filings: NLP Topic Modeling & Keyword Trend Analysis (LDA + SEC EDGAR, Reusable Template)"**

理由:
- **手法名（NLP Topic Modeling, LDA）** → 「LDA topic modeling time series」等の検索でヒットする
- **データソース名（SEC EDGAR）** → 再現可能性が明確
- **Reusable Template** → テーマ2 Notebook A/Bと同じ設計思想
- **30 Years** → スコープとスケール感
- 旧候補2「From 1,006 to 40,576...」はNotebook冒頭のリード文やSection 1の見出しに活用する

---

## セクション構成

### Section 0: Setup & Data Loading (3 cells)

- pip install + imports
- 10-Kテキストデータ（847チャンク）読み込み
- 店舗数時系列データ（30年×16列）読み込み
- キーワード頻度データ（30年×64列）読み込み

**使うデータ**: data/interim/ および data/processed/sec-edgar/ のCSV群

---

### Section 1: The Hook — From 1,006 to 40,576 (4 cells)

**図1**: 店舗数推移折れ線チャート（FY1996-FY2025）
- x軸=年度、y軸=全世界店舗数
- CEO在任期間を背景色バンドで区分（Schultz I / Smith / Schultz II / Johnson / Narasimhan / Niccol）
- FY2009（唯一のマイナス成長年）をアノテーション
- FY2025: 40,576店を終点ラベル

**コード**: 店舗数CSVの読み込み → matplotlib折れ線 + axvspan + annotate

**書く結論**: 30年で40倍。ほぼ一貫した右肩上がりだがFY2009のみ純減。CEO交代と成長率の変曲点が連動している。この成長の裏で、10-Kレポートの「語り方」はどう変わったのか？ → 以降のNLP分析への導入。

---

### Section 2: Text Preprocessing & Corpus Overview (3 cells)

**図2**: コーパス概要のサマリーテーブル
- 対象期間: FY1996-FY2025（30年分）
- 文書数: 30件（10-Kアニュアルレポート）
- チャンク数: 847（LDA用に分割済み）
- 前処理: セクション分割 → 段落チャンク化 → トークナイズ → ストップワード除去

**コード**: テキストデータのロード → 年度別文書長（トークン数）の棒グラフ

**書く結論**: 10-Kの文書量自体がFY1996（短い）→ FY2025（長大化）と増加しており、開示要件の拡大を反映している。キーワード頻度分析では相対頻度（出現回数/総トークン数）を使うことで文書量の差を正規化する。

---

### Section 3: Keyword Frequency Analysis — 6 Key Findings (6 cells)

30年×64キーワードの相対頻度マトリックスから、6つのKey Findingを順に提示。

**図3a**: "coffee" の相対頻度推移（折れ線）
- **Finding 1**: 「coffee」が30年間で62%減少。皮肉にも、コーヒー企業がコーヒーを語らなくなった。

**図3b**: "experience" の相対頻度推移（折れ線）
- **Finding 2**: 「experience」がゼロからピークへ。「第三の場所（Third Place）」戦略への転換を言語が反映。

**図3c**: "partner" vs "employee" の相対頻度推移（2本折れ線）
- **Finding 3**: FY2010を境に「partner」が「employee」を逆転。従業員の呼称変更が10-Kに反映された時点を特定。

**図3d**: "digital" + "mobile" の合算頻度 vs 店舗数（2軸チャート）
- **Finding 4**: デジタル/モバイル言及頻度と店舗数の相関 r=0.90。デジタル戦略の言語化と物理的拡大が同期。

**図3e**: その他の注目キーワード群（ヒートマップまたは小さな折れ線群）
- **Finding 5-6**: 残り2つの知見（例: "sustainability"/"ESG" の急増、"China"/"international" の変化等）

**コード**: キーワード頻度CSVの読み込み → 各Finding用の可視化 → 相関係数の計算

**書く結論**: キーワード頻度の変化は経営戦略の転換点と一致する。ただしキーワード分析は事前に選んだ単語しか追えない → 次のLDAで「事前知識なしのトピック検出」を行う。

---

### Section 4: LDA Topic Modeling — 7 Topics on 847 Chunks (4 cells)

**図4a**: 7トピックのワードクラウドまたはトップ10単語バーチャート
- 各トピックのラベル（手動命名）:
  - Topic 1: Store Operations / Retail
  - Topic 2: Financial Performance
  - Topic 3: Supply Chain / Product
  - Topic 4: Market Expansion / International
  - Topic 5: People / Culture / ESG
  - Topic 6: Digital / Technology
  - Topic 7: Risk / Legal / Compliance

**図4b**: 年度別トピック構成比のスタックエリアチャート（30年×7トピック）
- **Key Finding**: Topic 5（People/Culture/ESG）がFY2020以降に <10% → 25-30% へ急増。COVID-19とBLM以降の企業文化・ESG開示の爆発的増加を可視化。

**コード**: LDA結果CSVの読み込み → pyLDAvis的な可視化（静的版）→ stacked area chart

**書く結論**: LDAはキーワード分析では捕捉できなかった「トピック構成比の構造変化」を検出した。特にPeople/Culture/ESGトピックの急増はFY2020を境に明確であり、外部ショック（パンデミック・社会運動）が企業の語りを根本的に変えたことを示す。

---

### Section 5: NLP x Store Count — Correlation Analysis (3 cells)

**図5**: NLP指標 × 店舗数の相関マトリックス（ヒートマップ）
- 行: 主要キーワード頻度 + トピック構成比
- 列: 店舗数（全世界 / US / International）、成長率
- 注目セル: "digital+mobile" vs store_count r=0.90、Topic 4 (International) vs international_stores r=?

**コード**: キーワード頻度 + LDAトピック比率 + 店舗数時系列を年度キーで結合 → pearsonr → seaborn heatmap

**書く結論**: テキストの言語変化と物理的な店舗拡大は独立した現象ではなく、強い相関を持つ。ただし相関は因果ではない — デジタル言及が増えたから店舗が増えたのではなく、両者が同じ経営戦略から生まれた結果である可能性が高い。

---

### Section 6: Hero Chart — The 30-Year Starbucks Story in 4 Panels (3 cells)

**図6**: 4パネル統合チャート（2×2 または 1×4 縦並び、x軸=FY共通）

| パネル | 内容 | チャートタイプ |
|---|---|---|
| Panel A | 店舗数推移（CEO区分付き） | 折れ線 + 背景バンド |
| Panel B | キーワード頻度ハイライト3本 | 折れ線（coffee / experience / digital+mobile） |
| Panel C | LDAトピック構成比 | スタックエリア |
| Panel D | 選択した相関ペアのスキャッタ or デュアルライン | 散布図 or 2軸折れ線 |

- 4パネルのx軸を揃え、垂直方向に「同じ年の出来事」を視覚的に対応させる
- CEO交代年を全パネル共通の垂直点線で表示
- figsize=(16, 20) 程度の大判チャート

**コード**: matplotlib subplot + 共通x軸 + 統一スタイル

**書く結論**: この1枚のチャートが、30年間のスターバックスの「成長の物語」をデータで語る。店舗数の推移（Panel A）の裏で、企業の語りがどう変化し（Panel B, C）、両者がどう連動していたか（Panel D）を統合的に示す。

---

### Section 7: Limitations & What's Next (2 cells)

**制約の明記**:

| 制約 | 影響 | 緩和策 |
|---|---|---|
| 10-K のみ対象 | 決算説明会・プレスリリース等の情報を欠く | 10-Kは法定開示であり比較可能性が最も高い |
| LDAトピック数=7の選択 | トピック数は恣意的 | coherence score で複数候補を比較し7を選択（Week 6で実施済み） |
| 相対頻度の正規化 | 文書構造の変化（セクション追加等）を完全には排除できない | セクション単位の分析は将来課題 |
| 単年スナップショット | 10-K提出日と会計年度のラグ | FY（会計年度）ベースで統一 |
| 英語のみ | 中国語・日本語レポートの分析は対象外 | 全米＋グローバル店舗数で代替 |

**未実装: US全体の空間アニメーション**:
- 州別スタバ店舗数の30年間の拡大をアニメーション化する構想
- 追加データ（州別年次店舗数）が必要
- 本Notebookのスコープ外。将来的に追加セクションまたは別Notebookとして実装

**テーマ2への導線**:
> *"This notebook analyzed Starbucks' 30-year story at the national level through NLP and time series. For a deep dive into spatial strategy at the street level, see Theme 2: Manhattan Café Wars."*

---

## 依存するデータ

### 既存データ（Week 6で作成済み）

| ファイル | 場所 | 内容 |
|---|---|---|
| キーワード頻度マトリックス | data/interim/ or data/processed/sec-edgar/ | 30年×64列。各年度の相対キーワード頻度 |
| LDAトピック結果 | data/interim/ or data/processed/sec-edgar/ | 847チャンク×7トピックの構成比 + 年度別集約 |
| 店舗数時系列 | data/interim/ or data/processed/sec-edgar/ | 30年×16列。全世界/US/International等 |
| 10-Kテキストチャンク | data/processed/sec-edgar/ | 847チャンク。前処理済みテキスト |

### 未取得データ（空間アニメーション用 — 本Notebook対象外）

| データ | 取得方法 | 用途 |
|---|---|---|
| 州別年次店舗数（30年分） | 10-Kから手動抽出 or Starbucks IR資料 | US全体の空間的拡大アニメーション |

---

## セル数見積もり

| Section | コード | マークダウン | 計 |
|---|---|---|---|
| 0: Setup | 2 | 1 | 3 |
| 1: Hook (Store Count) | 2 | 2 | 4 |
| 2: Text Preprocessing | 2 | 1 | 3 |
| 3: Keyword Frequency | 4 | 2 | 6 |
| 4: LDA Topics | 3 | 1 | 4 |
| 5: NLP x Store Count | 2 | 1 | 3 |
| 6: Hero Chart | 2 | 1 | 3 |
| 7: Limitations | 0 | 2 | 2 |
| **合計** | **17** | **11** | **28** |

目標 28 cells、読了 15-25分。Notebook B の 24 cells とほぼ同規模。
