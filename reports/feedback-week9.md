# Week 9 Feedback Report — Day 5 (2026-03-14)

**Period reviewed:** 2026-03-13 (publish date) to 2026-03-14 (~1 day)

---

## 1. Notebook Metrics

| Notebook | Votes | Views* | Comments* | Forks* | Status |
|----------|-------|--------|-----------|--------|--------|
| Theme 0 — Manhattan Cafe Wars | 1 | N/A | N/A | N/A | Published |
| Theme 1 — 10-K NLP | 0 | N/A | N/A | N/A | Published |
| Notebook A — Spatial Clustering | 1 | N/A | N/A | N/A | Published |
| Notebook B — Location Fitness | 1 | N/A | N/A | N/A | Published |
| Notebook C — Data Pipeline | 0 | N/A | N/A | N/A | Published (2026-03-14) |

*Views/Comments/Forks not available via Kaggle kernels list API. Manual check on Kaggle web recommended.

## 2. Dataset Metrics

| Dataset | Views | Downloads | Kernels Using | Usability Rating | Votes |
|---------|-------|-----------|---------------|-----------------|-------|
| manhattan-cafe-wars | 30 | 0 | 4 | 0.53 (52.9%) | 0 |
| starbucks-30year-nlp-corpus | 1 | 0 | 2 | 0.65 (64.7%) | 0 |

## 3. Analysis

### Positive signals
- **3 notebooks have 1 vote each** (Theme 0, Notebook A, Notebook B) — someone is engaging with the work
- **Manhattan dataset: 30 views** in ~1 day — modest but nonzero discovery
- **4 kernels linked** to manhattan-cafe-wars — all 4 analysis notebooks are correctly associated
- **Notebook C published** and linked to both datasets — complete series now live

### Concerns
- **NLP Corpus dataset: only 1 view** — very low discoverability
- **0 downloads** on both datasets — viewers haven't engaged beyond browsing
- **Usability ratings are low** (53% and 65%) — Kaggle deprioritizes datasets below ~0.8
- **0 comments/forks** — expected at this early stage, but worth monitoring

### Root cause of low discoverability
1. **No tags on notebooks** (now partially addressed — see Section 4)
2. **Usability rating below 0.8** — likely caused by missing cover image and tags on dataset
3. **No Discussion posts** — no entry point from Kaggle community forums
4. **Title SEO** — "Manhattan Cafe Wars" is catchy but doesn't contain high-traffic search terms like "spatial analysis" or "geospatial"

## 4. SEO Actions Taken (2026-03-14)

### 4.1 Notebook Tags — Applied

Kaggle's tag system is **extremely limited**. Only a small set of predefined tags are accepted. We tested ~100+ candidates and found only ~15 valid tags total.

**Valid Kaggle tags discovered:**
`eda`, `nlp`, `clustering`, `classification`, `regression`, `data-visualization`, `deep-learning`, `neural-networks`, `feature-engineering`, `data-cleaning`, `text-mining`, `image-classification`, `text-classification`, `binary-classification`, `multiclass-classification`

**Tags applied per notebook:**

| Notebook | Tags Applied |
|----------|-------------|
| Theme 0 | `eda`, `data-visualization`, `clustering` |
| Theme 1 | `nlp`, `text-mining`, `data-visualization` |
| Notebook A | `clustering`, `eda`, `data-visualization` |
| Notebook B | `regression`, `feature-engineering`, `eda` |
| Notebook C | `data-cleaning`, `nlp`, `feature-engineering` |

**Note:** Domain-specific tags (`geospatial`, `spatial-analysis`, `openstreetmap`, `starbucks`, `manhattan`, `pysal`, `topic-modeling`, `sec-edgar`) are all **invalid** in Kaggle's tag system. This limits our ability to target niche audiences via tags. SEO must rely on title, subtitle, and description keywords instead.

### 4.2 Dataset Description Updates — Applied

Added Notebook C link to both dataset descriptions via API:
- `manhattan-cafe-wars`: Notebook C added to "Related notebooks" table
- `starbucks-30year-nlp-corpus`: Notebook C added to "Related notebooks" table

**Note:** Kaggle's metadata update API has a bug (json.load followed by json.loads). Worked around by calling the REST API directly. Keywords/tags were rejected by the API — need to be added manually via Kaggle web UI.

### 4.3 Dataset Usability Score — Manual Actions Needed

To improve usability from 0.53/0.65 to 0.8+, the following manual actions on Kaggle web are needed:

1. **Upload custom cover images** — hero chart from each notebook would be ideal
2. **Add tags via web UI** — API rejects keywords; web UI may have different tag options
3. **Verify column descriptions** — may need per-column descriptions in the Kaggle dataset editor (separate from the markdown description field)

### 4.4 Discussion Post — Not Yet Done

Deferred to after manual usability improvements. Suggested approach:
- Post in Kaggle "Getting Started" or "General" discussion
- Technical angle: "Analyzing 30 years of Starbucks expansion with NLP + spatial data science"
- Link to all 5 notebooks and 2 datasets
- Avoid promotional tone; focus on methodology and findings

## 5. Comparison to Benchmarks

For a brand-new Kaggle account with no followers:
- **30 dataset views in 1 day** is within normal range
- **3 votes across 5 notebooks** is slightly above average for Day 1
- **0 downloads** is typical — downloads usually lag views by several days
- The real test will be at the 1-week and 1-month marks

## 6. Test Kernels Created (Cleanup Needed)

During tag testing, 3 private test kernels were created:
- `tag-test-temp`
- `tag-test-temp-2`
- `tag-test-temp-3`

These are private and don't affect public visibility. Delete manually via Kaggle web UI when convenient.

## 7. Manual SEO Actions Completed (2026-03-14)

### Cover images uploaded
- manhattan-cafe-wars: 2-panel scatter map (Starbucks vs competitors + Location Fitness Score)
- starbucks-30year-nlp-corpus: 4-panel hero chart (store count + keywords + LDA + ESG surge)

### Dataset tags added via web UI

| Dataset | Tags |
|---------|------|
| manhattan-cafe-wars | Geospatial Analysis, Data Visualization, Exploratory Data Analysis, Cities and Urban Areas, Restaurants |
| starbucks-30year-nlp-corpus | NLP, Text Mining, Time Series Analysis, Business, Data Visualization |

### Usability score progression

| Dataset | Initial | +Cover Image | +Tags | Total Gain |
|---------|---------|-------------|-------|------------|
| manhattan-cafe-wars | 0.53 | 0.59 | 0.71 | +18pt |
| starbucks-30year-nlp-corpus | 0.65 | 0.71 | 0.71 | +6pt |

## 8. Next Steps

| Priority | Action | Owner |
|----------|--------|-------|
| 1 | Write Discussion post (technical angle) | Next session |
| 2 | Re-check all metrics at 2026-03-20 (1 week) | Next session |
| 3 | Delete 3 test kernels (manual) | User |
