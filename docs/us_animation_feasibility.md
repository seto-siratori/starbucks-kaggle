# US Expansion Animation — Feasibility Study

**Date:** 2026-03-14
**Context:** Theme 1 originally planned a "spatial time-series animation" of Starbucks' US expansion. This document evaluates whether it's achievable given available data.

---

## 1. The Core Problem: No Opening Dates

An ideal "dots appearing on a map" animation requires per-store opening dates. **No publicly available dataset provides this.**

| Data Source | Stores | Years | State-Level | Opening Dates | Coordinates |
|------------|--------|-------|-------------|---------------|-------------|
| 10-K timeseries (ours) | US total | 1996–2025 (30yr) | No | No | No |
| Kaggle directory.csv (2017) | 13,608 US | 2017 snapshot | Yes (51 states) | No | Yes |
| Kaggle 2023 snapshot | ~16,000 US | 2023 snapshot | Yes | No | Yes |
| GitHub chrismeller | ~16,000 US | 2020–present (daily) | Yes | Yes (inferred from diffs) | Yes |
| ScrapeHero | ~16,000 US | 2020–present | Yes | No | No |

**Verdict:** Individual store coordinate animation (dots growing on a map) is **not possible** for the full 30-year span.

---

## 2. What IS Possible: Three Feasible Alternatives

### Option A: State-Level Choropleth Slider (Recommended)

**Concept:** Animated choropleth map showing "stores per 100K population" by state, sliding from FY1996 to FY2025.

**Method:**
1. Use 2017 Kaggle snapshot for state-level proportions (CA=20.7%, TX=7.7%, WA=5.6%, ...)
2. Assume state shares are **roughly constant** over time (strong assumption but defensible — see Section 3)
3. Multiply each year's national US total by state share → estimated state-level count per year
4. Normalize by ACS state population (available by decade, interpolable) → stores per 100K
5. Render as Plotly choropleth with year slider or animation frame

**Strengths:**
- Full 30-year span (1996–2025)
- Visually compelling — shows geographic spread of saturation
- National totals from 10-K are high quality (our own extraction)
- Population normalization reveals density, not just raw count

**Weaknesses:**
- State shares assumed constant (see Section 3 for validation)
- Only 1 calibration point (2017 snapshot)
- Cannot show intra-state variation (no county/city granularity)

**Data requirements:** ✅ All available (store_counts_timeseries.csv + directory.csv + Census population by state)

### Option B: Dot Animation for 2020–2025 Only (Partial)

**Concept:** Use chrismeller/GitHub daily diffs to get actual store openings (coordinates + date) from 2020 onward.

**Strengths:**
- Real opening dates and coordinates
- Shows actual expansion patterns

**Weaknesses:**
- Only 5 years (2020–2025), not 30
- Requires scraping/parsing GitHub commit history
- Starbucks growth was slow in this period (COVID era), so less dramatic visually

**Verdict:** Interesting but limited scope. Could be a companion visual, not the main animation.

### Option C: National Growth Bar Chart Race

**Concept:** Animated bar chart showing US vs International store counts racing over 30 years, split by company-operated vs licensed.

**Strengths:**
- Uses our existing 10-K data directly, no approximation
- Simple, clean, attention-grabbing format
- Shows the US→International strategic pivot clearly

**Weaknesses:**
- Not spatial (no map)
- Less novel — bar chart races are common

---

## 3. Validating the "Constant State Share" Assumption

Can we assume California's ~20.7% share of US stores held roughly constant from 1996–2025?

**Supporting evidence:**
- The 2017 snapshot (13,608 stores) vs 10-K FY2017 total (13,930) differ by only 322 stores (2.3%), confirming the snapshot is representative
- Starbucks' US expansion was relatively uniform after initial West Coast concentration — by 2000, all 50 states had stores
- Academic literature on chain retail expansion suggests geographic shares stabilize after the initial growth phase

**Known violations:**
- **Early years (1996–2002):** Starbucks was heavily concentrated in WA/CA/OR. Applying 2017 shares to 1996 would **overestimate** non-West Coast states
- **Recent shifts:** Drive-through format expansion favors suburban/Southern states, slightly increasing TX/FL share vs WA/NY

**Mitigation:**
- Add a "confidence band" visualization: solid line for 2010–2025 (higher confidence), dashed/faded for 1996–2010 (lower confidence)
- Explicitly note the assumption in the notebook
- Optionally: use a 2-point calibration if we can get the 2023 Kaggle snapshot as a second anchor

**Conclusion:** The constant-share assumption is **reasonable for 2005–2025** but **weak for 1996–2005**. With proper caveats, this is acceptable for an exploratory visualization.

---

## 4. Data Pipeline for Option A

```
Step 1: State shares from 2017 snapshot
  directory.csv → group by State → share_pct per state

Step 2: National US totals (30 years)
  store_counts_timeseries.csv → us_total column

Step 3: Estimated state counts
  estimated_state_count[state][year] = us_total[year] × share_pct[state]

Step 4: State population (normalization)
  Census ACS 5-year estimates → state population by year
  (Available via Census API or pre-downloaded tables)

Step 5: Stores per 100K
  density[state][year] = estimated_count / population × 100,000

Step 6: Animation
  Plotly choropleth_map with animation_frame=fiscal_year
```

**New data needed:** Census state population by year (free, API or download from data.census.gov)

---

## 5. Recommendation

**Go with Option A (State-Level Choropleth Slider)** as the primary visualization.

- It leverages our existing 10-K timeseries (30 years of high-quality data)
- It's visually compelling and tells a clear story
- The constant-share assumption is transparent and well-documented
- Optionally add Option C (bar chart race) as a secondary visual in the same notebook

**Estimated effort:** 1 notebook, ~2 sessions to build + polish

**Notebook title candidate:** "Starbucks US Expansion: 30 Years of State-Level Growth (Animated Choropleth)"

---

## 6. Decision

| Option | Feasibility | Visual Impact | Data Quality | Recommendation |
|--------|------------|---------------|--------------|----------------|
| A: State choropleth slider | ✅ High | ⭐⭐⭐⭐ | Medium (assumption) | **Primary** |
| B: Dot animation (2020+) | ⚠️ Medium | ⭐⭐⭐⭐⭐ | High (but 5yr only) | Future add-on |
| C: Bar chart race | ✅ High | ⭐⭐⭐ | High | Secondary visual |
