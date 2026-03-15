# Week 8 Review — Theme 1 NLP Notebook Complete

**Period:** 2026-03-13 (Day 1–6)
**Author:** Claude Code (AI assistant)

---

## 1. Summary

Week 8 delivered the Theme 1 NLP notebook from design to Kaggle publication. The notebook analyzes 30 years of Starbucks 10-K filings (FY1996–FY2025) using keyword frequency analysis, LDA topic modeling, and NLP × store count correlation.

**Published artifacts:**

| Artifact | URL | Status |
|----------|-----|--------|
| Theme 1 Notebook | https://www.kaggle.com/code/shiratoriseto/starbucks-10-k-nlp-topic-keyword-analysis | Public, Run All passed |
| NLP Corpus Dataset | https://www.kaggle.com/datasets/shiratoriseto/starbucks-30year-nlp-corpus | Public, v1 |
| Theme 0 Notebook | https://www.kaggle.com/code/shiratoriseto/manhattan-cafe-wars-starbucks-vs-1200-competitors | Public |
| Notebook A (Spatial Clustering) | https://www.kaggle.com/code/shiratoriseto/starbucks-spatial-clustering | Public, Run All passed |
| Notebook B (Location Fitness) | https://www.kaggle.com/code/shiratoriseto/starbucks-location-fitness | Public, Run All passed |
| Manhattan Cafe Wars Dataset | https://www.kaggle.com/datasets/shiratoriseto/manhattan-cafe-wars | Public, v3 |

---

## 2. Theme 1 Notebook — Completion Details

### 2.1 Structure (38 cells, 7 sections + title)

| Section | Content | Figures |
|---------|---------|---------|
| 0 — Setup | pip install, imports, Kaggle/local path auto-detect, load 4 CSVs | — |
| 1 — The Hook | Store count by CEO era, Licensed % / International % | Fig. 1–2 |
| 2 — The Corpus | Corpus overview stats, word count bar + lexical diversity | Fig. 3 |
| 3 — Keyword Frequency | 6 findings: coffee decline, experience rise, partner vs employee crossover, china peak, digital+mobile surge, digital×stores r=0.90 | Fig. 4–9 |
| 4 — LDA Topic Modeling | 7-topic stacked area, People/ESG surge focus | Fig. 10–11 |
| 5 — NLP × Store Count | Correlation heatmap, 3-panel dual-axis | Fig. 12–13 |
| 6 — Hero Chart | matplotlib 4-panel summary figure | Fig. 14 |
| 7 — Limitations & Next Steps | 5 limitations table, Theme 2 links, Notebook C teaser | — |

### 2.2 Key Findings from the Analysis

1. **"coffee" declined 57%** — from 222/10K words (FY1996) to 95/10K (FY2025). The company that sells coffee talks less about coffee.
2. **"experience" emerged** as a core strategic word, peaking at 32/10K (FY2023). Reflects the "Third Place" pivot.
3. **"partner" overtook "employee(s)"** in the 10-K — a measurable trace of Schultz's philosophy in SEC filings.
4. **"china" peaked (FY2018, 42/10K) then retreated** — the 10-K as geopolitical barometer.
5. **"digital"+"mobile" went from zero to 30/10K** — language preceded the Mobile Order & Pay rollout.
6. **digital language × store count: r = 0.90** (p < 0.001) — 81% shared variance.
7. **People/Culture/ESG topic surged 3.6×** post-2020 (7.5% → 27.5%), the biggest structural break in 30 years.

### 2.3 Reusable Components

- `compute_keyword_trends()` function — works on any corpus of annual documents
- Full topic label/color mapping for 7-topic LDA
- Kaggle/local path auto-detection pattern

---

## 3. Dataset Architecture Decision

**Decision:** Created a new independent dataset `starbucks-30year-nlp-corpus` rather than adding NLP files to `manhattan-cafe-wars`.

**Rationale:**
- Theme 1 (NLP, national/global scope) and Theme 2 (spatial, Manhattan-only) are conceptually distinct
- Separate datasets allow Kagglers to use spatial data or NLP data independently
- Keeps each dataset focused and discoverable
- Avoids bloating the Manhattan dataset with unrelated files

**NLP Corpus Dataset contents (4 files, 26KB total):**

| File | Rows × Cols | Description |
|------|-------------|-------------|
| store_counts_timeseries.csv | 30 × 16 | Store counts by segment + CEO labels |
| item1_keyword_timeseries.csv | 30 × 70 | 34 keywords: raw counts + per-10K-words frequency |
| item1_lda_topic_proportions.csv | 30 × 8 | 7-topic LDA proportions by year |
| item1_basic_stats.csv | 30 × 6 | Word count, sentence count, lexical diversity |

---

## 4. Kaggle Execution Verification

### 4.1 Theme 1 Notebook — Kaggle Run All

- **Status:** COMPLETE (no errors)
- **Data source:** `/kaggle/input/datasets/shiratoriseto/starbucks-30year-nlp-corpus`
- **Output:** hero_chart.png generated
- **Key outputs verified:**
  - All 14 figures rendered
  - coffee decline = 57% (matches title punchline)
  - Pearson r = 0.902 (digital×stores)
  - People/ESG 3.6× increase
- **stderr:** Only warnings (SyntaxWarning from mistune, FutureWarning from traitlets) — no actual errors

### 4.2 LDA Reproducibility Note

The LDA topic proportions are **pre-computed** and shipped as CSV, so there is no gensim dependency or reproducibility risk on Kaggle. The notebook reads the pre-computed results directly. This was a deliberate design decision:
- No gensim install needed on Kaggle
- No random seed sensitivity
- Consistent topic proportions across runs
- Faster execution (~30 seconds total)

If a reader wants to retrain the LDA model, the preprocessing pipeline will be documented in Notebook C.

---

## 5. Notebook Polish (Day 5)

Issues found and fixed during review:

| Issue | Location | Fix |
|-------|----------|-----|
| coffee numbers wrong in punchline | Title cell | 348→222, 132→95, 62%→57% (aligned with CSV data) |
| Word count growth overstated | Section 2 takeaway | "3–4× longer" → "nearly doubled" (actual: 1.9×) |
| Word count range wrong | Section 2 takeaway | "~10,000+ words" → "~5,500 words" (actual FY2025: 5,498) |
| keyword count description | Section 0 intro | "30+" → "34" strategic keywords |
| Dataset reference URL | Section 0 intro | Updated to new dataset slug |
| Kaggle path | Setup cell | Changed from manhattan-cafe-wars to starbucks-30year-nlp-corpus |
| Subtitle too long | Dataset metadata | Shortened to 75 chars (Kaggle 80-char limit) |
| Title too long | Dataset metadata | Shortened to 33 chars (Kaggle 50-char limit) |

---

## 6. Public Notebook Feedback (as of 2026-03-13)

All notebooks were published on the same day (2026-03-13). No engagement yet, which is expected for Day 0.

| Notebook | Votes | Views | Comments | Forks |
|----------|-------|-------|----------|-------|
| Theme 0 (Manhattan Cafe Wars) | 0 | N/A* | 0 | 0 |
| Notebook A (Spatial Clustering) | 0 | N/A* | 0 | 0 |
| Notebook B (Location Fitness) | 0 | N/A* | 0 | 0 |
| Theme 1 (10-K NLP) | 0 | N/A* | 0 | 0 |

*View counts not available via Kaggle API. Manual check recommended after 1 week.

**Action items for Week 9:**
- Re-check metrics after 7 days (by 2026-03-20)
- If views > 0 but votes = 0, consider improving thumbnail/title/description
- If comments appear, respond within 24 hours

---

## 7. Notebook C — Design Direction

Notebook C will document the **data preprocessing pipeline** for the NLP corpus:

**Scope:**
1. SEC EDGAR 10-K download (CIK lookup, filing index, rate-limited fetching)
2. Item 1 section extraction (HTML/XBRL parsing, regex boundary detection)
3. Text preprocessing (tag stripping, whitespace normalization, tokenization)
4. Keyword frequency computation (using `compute_keyword_trends()`)
5. LDA topic modeling (gensim, chunk creation, coherence-based k selection)
6. Output CSV generation

**Key decisions to make:**
- Whether to run the full pipeline on Kaggle (EDGAR rate limits + ~30 min runtime) or provide it as documentation-only
- If documentation-only, whether to include a small demo (e.g., download 1 filing and process it) for interactivity
- Whether to include the raw 10-K texts in the dataset (public domain, but ~2MB for 30 files)

---

## 8. Week 9 Plan

| Priority | Task | Estimated Effort |
|----------|------|-----------------|
| 1 | Notebook C design & implementation (data pipeline documentation) | 2–3 days |
| 2 | Re-check Kaggle feedback metrics (after 7 days) | 0.5 day |
| 3 | Feedback-driven fixes (if comments appear) | As needed |
| 4 | Cross-link all notebooks (Theme 0 ↔ Theme 1 ↔ Theme 2) | 0.5 day |
| 5 | Consider SEO: add tags, improve descriptions, write discussion posts | 1 day |
| 6 | Explore: US-wide store animation (if time permits) | 2–3 days |

**Risk:**
- Notebook C's scope could expand if we include a full runnable EDGAR pipeline. Recommend scoping to "download 1 filing + process it" as an interactive demo, with the full 30-year pipeline as documented code.

---

## 9. Project Status Overview

| Theme | Notebooks | Dataset | Kaggle Status |
|-------|-----------|---------|---------------|
| Theme 0 | Manhattan Cafe Wars (1 notebook) | manhattan-cafe-wars v3 | Published |
| Theme 1 | 10-K NLP Analysis (1 notebook) | starbucks-30year-nlp-corpus v1 | Published, Run All passed |
| Theme 2 | Spatial Clustering + Location Fitness (2 notebooks) | manhattan-cafe-wars v3 | Published, Run All passed |
| Pipeline | Notebook C (planned) | TBD | Not started |

**Total published:** 4 notebooks, 2 datasets, 14 figures in Theme 1 alone.
