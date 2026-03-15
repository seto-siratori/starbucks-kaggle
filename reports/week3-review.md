# Week 3 レビュー

作成日: 2026-03-13

---

## 実施したこと

| Day | タスク | 対象 |
|---|---|---|
| Day 1 | Theme 0 Notebook 構成設計（outline.md） | テーマ0 |
| Day 2 | Dataset用CSV 3ファイル作成 + metadata.json | テーマ0 |
| Day 3 | Kaggle Dataset アップロード + Notebook Section 0-3 初版 | テーマ0 |
| Day 4 | Notebook Section 1-3 リファクタ（pathlib, 赤色統一, 3距離分析追加） | テーマ0 |
| Day 5 | Section 4-5 コーディング（OSMnxデモ→最寄りスタバ歩行距離, Kaggle互換） | テーマ0 |
| Day 6 | マークダウン推敲 + チェックリスト検証 + 公開 + 振り返り | テーマ0 |

---

## 公開物

| 種別 | URL | ステータス |
|---|---|---|
| Dataset | https://www.kaggle.com/datasets/shiratoriseto/manhattan-cafe-wars | 公開待ち（Private） |
| Notebook | （Kaggle Notebookにアップロード後に記入） | 未アップロード |

---

## Notebook 最終構成

| Section | セル数 | 内容 |
|---|---|---|
| 0: Setup & Data Loading | 4 | pip install, import, pathlib auto-detect, brand breakdown |
| 1: The Map | 2 | folium 4層マップ（Starbucks赤, Dunkin'橙, Other灰, MTA青） |
| 2: Density | 5 | 棒グラフ, ゾーン別積み上げ, 密度ヒートマップ（plotly Densitymapbox） |
| 3: Distance Analysis | 5 | KDTree 3距離計算, 3パネルヒストグラム, 最近接ペアテーブル |
| 4: OSMnx Demo | 4 | 歩行ネットワーク取得, 最短経路計算, foliumルートマップ |
| 5: What's Next | 1 | シリーズロードマップ + ライセンス表記 |
| **合計** | **23** | コード12 + マークダウン11 |

---

## チェックリスト結果

| 項目 | 結果 |
|---|---|
| 全セルがローカルで上から順に実行通過 | PASS |
| folium地図が表示される（show_map()でKaggle互換） | PASS |
| plotlyグラフがインタラクティブ | PASS |
| DatasetリンクがNotebook内に記載 | PASS |
| ライセンス表記（ODbL, OPEN NY）がNotebook内に記載 | PASS |
| Dataset metadata にライセンス記載 | PASS |
| pathlib.Pathでパス管理 | PASS |
| Kaggle Notebook上での動作確認 | **未実施**（公開後に実施） |

---

## 環境構築からここまでで一番詰まったポイント

1. **Kaggle CLIの認証** — `KAGGLE_API_TOKEN` の形式と設定方法に数回トライ。最終的に `export KAGGLE_API_TOKEN=KGAT_...` で解決
2. **MTA station_complex_id の重複** — 161エントリ中123ユニークID。複数プラットフォームが同一complex_idを共有しており、groupby dedup が必要だった
3. **OSMnxデモのペア選択** — 最近接ペア（53m）だとノードスナップにより歩行距離 < 直線距離になる逆転現象。150-350m範囲のペアに切り替えて解決
4. **MapPLUTO Shapefile 404** — 全URLパターンがダウンロード不可。CSV API + cKDTree nearest joinで代替し、100%マッチを達成
5. **Kaggle Dataset metadata制約** — タイトル50文字・サブタイトル80文字制限。数回の短縮調整が必要だった

---

## 公開時点の数字

| 指標 | 値 |
|---|---|
| Dataset upvotes | 0 |
| Dataset views | 0 |
| Notebook upvotes | — |
| Notebook views | — |

*初日の数字に意味はないが、基準点として記録*

---

## Week 4 でやるべきこと

### 優先度 P1（必須）

| タスク | 内容 |
|---|---|
| Kaggle Notebook 公開 | Notebook を Kaggle にアップロードし、Restart & Run All で動作確認後に公開 |
| 10-K 全量ダウンロード | SEC EDGAR から 29本の 10-K を一括取得（1996-1999 は手動） |
| セクション分割パイプライン構築 | 3フォーマット対応の Item 抽出モジュール (src/) |
| 店舗数時系列の抽出 | Item 1 から年次店舗数を regex で抽出 |

### 優先度 P2（できれば）

| タスク | 内容 |
|---|---|
| NLP プロトタイプ | Item 1 テキストでトピックモデリング or embedding |
| TIGER/Line Census Tract 取得 | マンハッタン Tract ポリゴン + ACS 所得・人口 |
| stores_enriched.csv 構築 | 結合設計書に基づき 171店 × ~30カラムの統合テーブル |

### 優先度 P3（余裕があれば）

| タスク | 内容 |
|---|---|
| MTA 全駅乗降データ取得 | 161駅×時間帯別の平均乗降数（3,683万行のチャンク処理） |
| 全米 Shapefile + ACS | 州境界ポリゴン + 州別人口で出店密度正規化 |

---

## リスクと注意事項

1. **OSMnx on Kaggle 未検証** — ローカルでは動作するが、Kaggle Notebook での pip install + Overpass API が通るか確認必要。Internet ON 必須
2. **10-K 1996-1999 の取得** — SEC EDGAR で 503 エラーが出る可能性。手動ダウンロード + 4年分欠損の可能性を許容する設計
3. **MTA 全量データのサイズ** — マンハッタン 3,683万行。API のページネーション + メモリ管理が必要
