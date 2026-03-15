# Week 9 Review Report

**Period:** 2026-03-10 (Mon) — 2026-03-14 (Fri)
**Author:** Claude Code (auto-generated)

---

## 1. Week Summary

Week 9 was the **publication & SEO week**. All planned notebooks and datasets are now live on Kaggle.

| Day | Work Done |
|-----|-----------|
| Day 1–2 | Notebook C (Data Pipeline) — Sections 0–3 built |
| Day 3 | Notebook C — Sections 4–6 (KDTree joins, data quality report, reproducibility guide) |
| Day 4 | Notebook C polish, Kaggle Run All debugging (ON_KAGGLE detection, Overpass rate limit), publish |
| Day 5 | Feedback metrics check, SEO optimization (tags, cover images, descriptions), Discussion post |
| Day 6 | Notebook thumbnails, US expansion animation feasibility study, Week 9 report |

---

## 2. Publication Status — All Assets Live

### Notebooks (5/5 published)

| # | Title | Votes | Last Run | Tags | Status |
|---|-------|-------|----------|------|--------|
| 0 | Manhattan Cafe Wars: Starbucks vs 1200 Competitors | 1 | 2026-03-14 | eda, data-visualization, clustering | ✅ Public |
| 1 | Starbucks 10-K NLP: Topic & Keyword Analysis | 0 | 2026-03-14 | nlp, text-mining, data-visualization | ✅ Public |
| A | Starbucks Spatial Clustering | 1 | 2026-03-14 | clustering, eda, data-visualization | ✅ Public |
| B | Starbucks Location Fitness | 1 | 2026-03-14 | regression, feature-engineering, eda | ✅ Public |
| C | Starbucks Data Pipeline: EDGAR & OSM to CSV | 0 | 2026-03-14 | data-cleaning, nlp, feature-engineering | ✅ Public |

### Datasets (2/2 published)

| Dataset | Views | Downloads | Votes | Usability | Tags |
|---------|-------|-----------|-------|-----------|------|
| Manhattan Cafe Wars | 34 | 0 | 0 | 0.71 | Geospatial Analysis, Data Visualization, EDA, Cities, Restaurants |
| Starbucks 30-Year NLP Corpus | 4 | 0 | 0 | 0.71 | NLP, Text Mining, Time Series Analysis, Business, Data Visualization |

### Other Assets

| Asset | Status |
|-------|--------|
| Discussion post (General forum) | ✅ Published |
| Dataset cover images | ✅ Uploaded (both datasets) |
| Notebook thumbnails | ✅ Added to all 5 notebooks (pending cache refresh) |
| Test kernels (tag-test-temp ×3) | ✅ Deleted |

---

## 3. Notebook C — Completion Details

Notebook C was the most complex deliverable of the week. Final structure:

- **30 cells** (15 code + 15 markdown), Sections 0–6
- **Live demos on Kaggle:** SEC EDGAR download (1 filing), Overpass API queries (with rate limit handling)
- **Data quality report:** Full 63-column audit, known anomalies, NLP corpus quality check
- **Reproducibility guide:** Step-by-step checklist to rebuild both datasets from scratch

**Issues encountered & resolved:**
1. ON_KAGGLE detection — changed from dataset path check to `Path("/kaggle/working").exists()`
2. Overpass API rate limiting — added `time.sleep(5)` + try/except fallback
3. Cell ordering — used Python JSON manipulation (NotebookEdit can't move cells)

---

## 4. SEO Optimization Summary

| Action | Impact |
|--------|--------|
| Notebook tags (valid Kaggle tags applied) | Improved discoverability in search |
| Dataset cover images uploaded | Usability: +6pt per dataset |
| Dataset tags added via web UI | Usability: +12pt per dataset |
| Dataset descriptions updated (Notebook C links) | Cross-linking between assets |
| Discussion post published | Entry point from community forums |
| Notebook thumbnails added | Visual appeal in search results (pending) |

**Usability score progression:**
- Manhattan Cafe Wars: 0.53 → 0.71 (+18pt)
- NLP Corpus: 0.65 → 0.71 (+6pt)
- Target of 0.8+ not yet reached — may need per-column descriptions in dataset editor

---

## 5. Feedback Metrics (Day 2 post-publish)

| Metric | Value | Assessment |
|--------|-------|------------|
| Total notebook votes | 3 (across 3 notebooks) | Slightly above average for new account |
| Dataset views | 38 (34 + 4) | Normal range for Day 2 |
| Downloads | 0 | Typical — usually lags views by days |
| Comments | 0 | Expected at this stage |
| Forks | 0 | Expected at this stage |

**Next metrics check:** 2026-03-20 (1 week post-publish)

---

## 6. US Expansion Animation — Feasibility Assessment

**Full analysis:** `docs/us_animation_feasibility.md`

### Key Findings

| Question | Answer |
|----------|--------|
| Do 10-K filings have state-level data? | No — only US total vs international |
| Does directory.csv have opening dates? | No — single 2017 snapshot |
| Can we approximate state-level growth? | Yes, with constant-share assumption (valid ~2005–2025) |
| Is a dot animation possible? | Not for full 30-year span (no per-store dates) |
| Is a choropleth animation possible? | **Yes** — recommended approach |

### Recommended Approach: State-Level Choropleth Slider

- 2017 Kaggle snapshot provides state shares (CA=20.7%, TX=7.7%, ...)
- Apply shares to 30-year national totals from 10-K → estimated state counts
- Normalize by Census state population → stores per 100K
- Render as Plotly choropleth with year slider/animation

**Data gap:** Need Census state population by year (free, available via Census API)

### Decision: **FEASIBLE — Proceed**

---

## 7. Next Phase Plan

### Immediate (Week 10)

| Priority | Task | Est. Sessions |
|----------|------|--------------|
| 1 | Download Census state population data | 0.5 |
| 2 | Build US expansion choropleth notebook | 2 |
| 3 | Polish & publish as Notebook D | 0.5 |
| 4 | Re-check metrics (2026-03-20) | 0.5 |

### Notebook D Design

- **Title candidate:** "Starbucks US Expansion: 30 Years of State-Level Growth (Animated Choropleth)"
- **Dataset dependency:** Uses existing store_counts_timeseries.csv + new Census population data
- **Visuals:** Animated choropleth (primary) + bar chart race US vs Intl (secondary)
- **Kaggle dataset:** May add state-level estimates to NLP Corpus dataset as new CSV

### Medium-Term Options

| Option | Description | Effort |
|--------|-------------|--------|
| Notebook D (above) | US expansion animation | 3 sessions |
| Small notebook: OSMnx walk analysis | Deep dive on walk-distance from Theme 0 | 1–2 sessions |
| Small notebook: LDA deep dive | Interactive topic explorer from Theme 1 | 1–2 sessions |
| Dataset usability to 0.8+ | Per-column descriptions in Kaggle editor | 1 session |

---

## 8. Risks & Blockers

| Risk | Severity | Mitigation |
|------|----------|------------|
| Constant-share assumption inaccurate for pre-2005 | Medium | Document limitation, use confidence bands |
| Notebook thumbnails not reflecting | Low | May take time; if persistent, investigate Quick Save vs Run All |
| 0 downloads on datasets | Low | Normal for early stage; monitor at 1-week mark |
| NLP Corpus low visibility (4 views) | Medium | Discussion post may help; consider cross-posting on Reddit/Twitter |
