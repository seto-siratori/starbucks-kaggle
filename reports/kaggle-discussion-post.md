# How I Used KDTree Spatial Joins + LDA Topic Modeling to Analyze Starbucks' 30-Year Expansion

I built a 5-notebook series analyzing Starbucks from two angles: **NLP on 30 years of SEC filings** and **spatial analysis of Manhattan store locations**. Sharing the methodology in case it's useful for anyone working with geospatial or text data.

## The data (all public, no scraping)

Everything comes from 7 free data sources — SEC EDGAR, OpenStreetMap, MapPLUTO, MTA ridership, Census ACS, TIGER/Line shapefiles, and NYC DOT pedestrian counts. Two datasets are published on Kaggle:

- [Manhattan Cafe Wars](https://www.kaggle.com/datasets/shiratoriseto/manhattan-cafe-wars) — 171 Starbucks × 63 columns (OSM + building + transit + demographics + competitor density)
- [Starbucks 30-Year NLP Corpus](https://www.kaggle.com/datasets/shiratoriseto/starbucks-30year-nlp-corpus) — keyword frequencies, LDA topic proportions, and store counts from FY1996–FY2025

## Techniques that worked well

### 1. cKDTree for spatial joins (scipy)

Instead of GeoPandas spatial joins (which need CRS transformations and can be slow), I used `scipy.spatial.cKDTree` with a simple planar projection:

```python
REF_LAT = 40.75
M_PER_DEG_LAT = 111_320
M_PER_DEG_LON = M_PER_DEG_LAT * np.cos(np.radians(REF_LAT))
```

At Manhattan's scale (~20 km), this introduces <0.5% error. Three joins run in under 1 second:
- **Nearest MapPLUTO lot** (k=1) → building attributes (median match: 21.3m)
- **Nearest MTA station** (k=1) → transit ridership (median: 195m)
- **Competitor density** (ball query at 250m/500m/1000m) → how crowded each location is

### 2. LDA topic modeling on SEC filings

I extracted Item 1 (Business) from 30 annual 10-K filings, chunked each into ~150-word segments (847 total), and trained a 7-topic LDA model. The most interesting finding: **People/Culture/ESG topic surged 3.6× after 2020** (7.5% → 27.5%), the largest structural break in 30 years of filings.

### 3. Location Fitness Score

A simple demand-supply framework: `LFS = demand_proxy - supply_index`, where demand combines MTA ridership + pedestrian counts + population density, and supply counts nearby cafes. This identifies underserved locations — and backtesting against 2024 store openings showed the model correctly ranked high-demand gaps.

## The notebooks

| # | Notebook | What it covers |
|---|----------|---------------|
| 0 | [Manhattan Cafe Wars](https://www.kaggle.com/code/shiratoriseto/manhattan-cafe-wars-starbucks-vs-1200-competitors) | EDA: 171 Starbucks vs 1,200+ competitors |
| 1 | [10-K NLP Analysis](https://www.kaggle.com/code/shiratoriseto/starbucks-10-k-nlp-topic-keyword-analysis) | Keyword trends, LDA topics, NLP × store count correlation |
| 2A | [Spatial Clustering](https://www.kaggle.com/code/shiratoriseto/starbucks-spatial-clustering) | Moran's I, LISA hotspots, Ripley's K |
| 2B | [Location Fitness](https://www.kaggle.com/code/shiratoriseto/starbucks-location-fitness) | Demand-supply scoring & backtest |
| C | [Data Pipeline](https://www.kaggle.com/code/shiratoriseto/starbucks-data-pipeline-edgar-osm-to-csv) | Full pipeline from EDGAR/OSM to CSV, with data quality report |

Notebook C documents the entire pipeline so everything is reproducible from raw public data.

## What I'd do differently

- **OSM coverage is ~85%** for Manhattan Starbucks. A Google Places API cross-check would close the gap, but adds cost.
- **LDA is stochastic** — I shipped pre-computed topic proportions as CSV to avoid reproducibility issues on Kaggle.
- **Pedestrian count data is sparse** (only 36 NYC DOT counters) — the nearest-counter proxy works but isn't ideal for locations far from a counter.

Happy to answer questions about any of the techniques. Feedback on the methodology is very welcome.
