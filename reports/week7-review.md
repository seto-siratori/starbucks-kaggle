# Week 7 レビュー

作成日: 2026-03-13

---

## 実施したこと

| Day | タスク | 対象 |
|---|---|---|
| Day 1 | Notebook B コーディング Section 0-2（Setup, Hook, Demand Proxy） | テーマ2 |
| Day 2 | Notebook B Section 3（LFSモデル構築 + ランキング） | テーマ2 |
| Day 3 | Notebook B Section 4（感度分析：需要重み3シナリオ + 競合重み3パターン） | テーマ2 |
| Day 4 | Notebook B Section 5-6（バックテスト + OSMnx歩行圏デモ） | テーマ2 |
| Day 5 | Notebook B Section 7（Limitations）+ 全体仕上げ（英文・図番号・数式統一） | テーマ2 |
| Day 6 | Dataset v3フォルダ準備 + テーマ1 Notebook構成設計 + Week 7レポート | テーマ1/2 |

---

## 分析結果サマリ

### Notebook B: "Where Should the 172nd Starbucks Go?"

#### 完成状態

- **30セル**（マークダウン9 + コード21）、Section 0-7 すべて実装済み
- `nbconvert --execute` で全セル通過（エラーゼロ）確認
- **11図**（Fig. 1-11）すべてナンバリング・キャプション統一済み

#### Location Fitness Score (LFS) モデル

**数式**: `LFS = Demand Proxy Index / (Supply Index + 1)`

| 構成要素 | 詳細 |
|---|---|
| Demand Proxy Index | MTA乗降客数(0.50) + 歩行者通行量(0.25) + 居住人口密度(0.25)、各min-max正規化 |
| Supply Index | N_starbucks + 0.5 × N_competitor_cafes |
| 再利用性 | `compute_lfs()` 関数化。引数にデータフレーム・重みを渡せば任意の都市で動作 |

#### Under-served上位（出店候補）

| 順位 | Census Tract | LFS | スタバ | 競合 | 特徴 |
|---|---|---|---|---|---|
| 1 | 158.02 | 0.143 | 1 | 0 | 需要に対して供給最少 |
| 2 | 101 | 0.140 | 2 | 3 | 需要が非常に高い |
| 3 | 145 | 0.139 | 1 | 1 | 需要に対して供給不足 |

#### Over-served上位（カニバリリスク）

| 順位 | Census Tract | LFS | スタバ | 競合 | 特徴 |
|---|---|---|---|---|---|
| 1 | 94 | 0.000 | 4 | 8 | LISA High-High |
| 2 | 82 | 0.003 | 4 | 10 | LISA High-High |

#### 感度分析結果

**需要重みシナリオ（3パターン）**:

| シナリオ | MTA | 歩行者 | 人口密度 | 説明 |
|---|---|---|---|---|
| Baseline | 0.50 | 0.25 | 0.25 | ベースライン |
| Transit-Heavy | 0.70 | 0.15 | 0.15 | 交通重視 |
| Balanced | 0.33 | 0.33 | 0.34 | 均等配分 |

**Spearman順位相関**: 全ペアで **ρ ≥ 0.89**（p < 0.001）。重みの選択に対してランキングはロバスト。

**競合重みシナリオ（3パターン）**:

| 競合重み | 意味 |
|---|---|
| 0.0 | 競合無視 |
| 0.5 | ベースライン |
| 1.0 | 競合を自社と等価 |

**Spearman順位相関**: 全ペアで **ρ ≥ 0.93**。競合の扱いを変えてもランキングは安定。

**Top 10 安定性**: 上位10のうち **7-8 Tract が全シナリオで共通**（★ Stable）。

#### バックテスト結果

- **データ**: 2017 Kaggle directory.csv（232店舗@Manhattan） vs 2026 OSM（171店舗）
- **手法**: cKDTree近接マッチング（500m閾値）
- **マッチ結果**: 207マッチ / 25件は2017のみ（閉店推定）
- **Mann-Whitney U検定**: 2017→2026で新規出店したTractは、出店しなかったTractよりLFSが有意に高い（**p < 0.001**）
- **解釈**: LFSモデルは過去の出店判断と統計的に整合。ただし座標精度（2桁）の制約あり

#### OSMnx歩行圏デモ

- 2店舗で400m歩行圏ポリゴンを計算（`compute_isochrone()` 関数）
- Folium地図上に表示（Fig. 11）
- フルバッチ用テンプレートコード提供

---

### Dataset v3

| 指標 | v2 | v3 |
|---|---|---|
| ファイル数 | 6 | 8 |
| 主な追加 | — | stores_enriched_v4.csv, tract_demand_supply.csv, manhattan_pedestrian_counts.csv |
| stores_enrichedバージョン | v3 (51列) | v4 (63列) |

追加ファイル:
- `stores_enriched_v4.csv`: 171行×63列（v3の51列 + Tract需給スコア12列）
- `tract_demand_supply.csv`: 309 Tract×24列（全Tractの需給スコア）
- `manhattan_pedestrian_counts.csv`: 36地点×113列（NYC DOT歩行者カウント 2007-2025）

metadata.json更新済み（全8ファイルのカラム説明、v3更新履歴追加）。

---

### テーマ1 Notebook構成設計

タイトル: **"From 1,006 to 40,576: How Starbucks Talked Its Way Through 30 Years of Growth"**

| Section | 内容 | セル数 |
|---|---|---|
| 0: Setup | pip install + データ読み込み | 3 |
| 1: Hook | 店舗数推移（CEO区分付き折れ線） | 4 |
| 2: Text Preprocessing | コーパス概要 + 文書長推移 | 3 |
| 3: Keyword Frequency | 6 Key Findings（coffee衰退、experience台頭、partner逆転、digital相関等） | 6 |
| 4: LDA Topics | 7トピック可視化 + 積み上げ面グラフ | 4 |
| 5: NLP x Store Count | 相関マトリックス | 3 |
| 6: Hero Chart | 4パネル統合チャート | 3 |
| 7: Limitations | 制約 + テーマ2への導線 | 2 |
| **合計** | | **28** |

設計書: `docs/notebook_theme1_outline.md`

---

## 成果物一覧

### テーマ2

| ファイル | 内容 |
|---|---|
| notebooks/02_theme2/notebook_b_location_fitness.ipynb | 30セル、Section 0-7完成、全セル実行確認済み |
| dataset-upload/v3/ | 8ファイル + dataset-metadata.json |
| dataset-upload/v3/stores_enriched_v4.csv | 171行×63列 |
| dataset-upload/v3/tract_demand_supply.csv | 309 Tract×24列 |
| dataset-upload/v3/manhattan_pedestrian_counts.csv | 36地点×113列 |

### テーマ1

| ファイル | 内容 |
|---|---|
| docs/notebook_theme1_outline.md | 28セル構成設計書 |

---

## テーマ0の公開状況

| 項目 | ステータス |
|---|---|
| Dataset | Private（電話番号認証待ち） |
| Notebook | Private（電話番号認証待ち） |
| 認証状況 | ユーザーが別途対応中 |

---

## 技術的な課題と解決

| 課題 | 解決策 |
|---|---|
| Section 1で未定義変数`demand`を参照 | LISA集計テーブルに差し替え、`tract_ds`読み込みをSection 0へ移動 |
| `applymap` 非推奨 | `map` + カスタム`highlight_stability()`関数に置換 |
| バックテストのTract空間結合失敗（座標精度2桁） | cKDTree近接マッチング（500m閾値）に方針変更 → 有意な結果を取得 |
| OSMnx `nearest_nodes`でscikit-learn要求 | `pip install scikit-learn` 追加 |
| LFS数式記述の不整合（>1/<1閾値表記 vs 実値0-0.15） | "High LFS / Low LFS / LFS=0" の定性表現に修正 |
| Fig. 9b/10の番号飛び | Fig. 1-11の連番に統一 |

---

## Week 8 でやるべきこと

### 優先度 P1（必須）

| タスク | 内容 |
|---|---|
| テーマ1 Notebook コーディング | notebook_theme1_outline.md に基づき Section 0-7 を実装（28セル） |
| Kaggle公開（認証通過時） | Dataset v3 + Notebook A/B push → Internet ON → Run All → Public |

### 優先度 P2（できれば）

| タスク | 内容 |
|---|---|
| Notebook B Kaggle互換性検証 | Kaggle環境でのRun All確認（OSMnx/foliumのバージョン差異） |
| Dataset v3 メタデータ最終確認 | カラム説明の正確性・欠損値ポリシーの最終チェック |
| テーマ1 Hero Chart プロトタイプ | 4パネル統合チャートの事前試作（matplotlibレイアウト確認） |

### 優先度 P3（余裕があれば）

| タスク | 内容 |
|---|---|
| 歩行者カウントの空間補間改善 | 36地点→309 TractへのIDW/Kriging補間 |
| 全米出店アニメーション設計 | store_counts_timeseries.csv + 州別データで密度マップ |
| LinkNYCキオスクデータ結合 | 需要代理変数の追加候補 |

---

## リスクと注意事項

1. **Kaggle電話番号認証** — ユーザーが別途対応中。テーマ0・2ともに公開がブロックされている
2. **OSMnx Kaggle互換性** — ローカルでは動作するがKaggle環境のOSMnxバージョンが異なる可能性。Section 6は`try/except`でフォールバック済み
3. **テーマ1のデータ同梱方針** — 10-Kテキスト自体は再配布可能だが、前処理済みチャンクをDatasetに含めるか検討が必要
4. **stores_enriched の版管理** — v1(44列)→v2(49)→v3(51)→v4(63)。Dataset v3ではv4のみ同梱。Notebook AはDataset内のv3ではなくv4で動作確認が必要
