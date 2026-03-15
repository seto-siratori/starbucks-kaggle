# Starbucks Spatial Data Science: A 9-Notebook Kaggle Series

A comprehensive spatial data science project using Starbucks as a case study — combining geospatial analysis of Manhattan's cafe market with NLP analysis of 30 years of SEC 10-K filings.

**100% open data. Fully reproducible on Kaggle.**

## Notebooks

| # | Notebook | Theme | Kaggle Link |
|---|----------|-------|-------------|
| 0 | Manhattan Cafe Wars | EDA & competitor mapping | [Open](https://www.kaggle.com/code/shiratoriseto/manhattan-cafe-wars-starbucks-vs-1200-competitors) |
| 1 | 10-K NLP Topic & Keyword Analysis | 30-year corporate language trends | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-10-k-nlp-topic-keyword-analysis) |
| 1F | LDA Topic Explorer (pyLDAvis) | Interactive topic visualization | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-10-k-lda-topic-explorer-pyldavis) |
| 2A | Spatial Clustering | Moran's I, LISA, Ripley's K | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-spatial-clustering) |
| 2B | Location Fitness | Demand-supply scoring & backtest | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-location-fitness) |
| 2C | Walk-Distance Analysis (OSMnx) | Network-based walk isochrones | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-walk-distance-analysis-osmnx) |
| C | Data Pipeline | EDGAR + OSM to CSV | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-data-pipeline-edgar-osm-to-csv) |
| D | US Expansion Choropleth | 30-year animated state-level map | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-us-expansion-animated-choropleth) |
| G | NLP x Spatial Cross-Theme | Did corporate language predict expansion? | [Open](https://www.kaggle.com/code/shiratoriseto/starbucks-nlp-x-spatial) |

## Datasets

| Dataset | Description | Kaggle Link |
|---------|-------------|-------------|
| Manhattan Cafe Wars | 171 Starbucks + 1,200 competitors, MTA ridership, Census, PLUTO | [Open](https://www.kaggle.com/datasets/shiratoriseto/manhattan-cafe-wars) |
| Starbucks 30-Year NLP Corpus | 10-K topic proportions, keyword time series, store counts (FY1996-2025) | [Open](https://www.kaggle.com/datasets/shiratoriseto/starbucks-30year-nlp-corpus) |

## Key Findings

- **Starbucks locations correlate with subway ridership (r=0.58) but NOT household income (r=0.03)** — they chase foot traffic, not wealth
- **Moran's I = 0.36 (p<0.001)** — store locations are statistically clustered, not random
- **Walk-distance vs straight-line** — Euclidean distance underestimates real walking distance by 20-40% in Manhattan's grid
- **10-K language is more mirror than crystal ball** — corporate language describes strategy already in motion rather than predicting future expansion
- **ESG & Digital topics surged post-2018** while Store Operations language declined, matching Manhattan's spatial saturation

## Project Structure

```
starbucks-kaggle/
  notebooks/           # Jupyter notebooks organized by theme
    00_theme0/         # Manhattan Cafe Wars (Notebook 0)
    01_theme1/         # NLP analysis (Notebooks 1, 1F)
    02_theme2/         # Spatial analysis (Notebooks 2A, 2B, 2C)
    03_pipeline/       # Data pipeline (Notebook C)
    03_us_expansion/   # US expansion animation (Notebook D)
    04_cross_theme/    # NLP x Spatial (Notebook G)
  src/                 # Reusable Python modules
  scripts/             # Data preparation scripts
  docs/                # Design documents & outlines
  reports/             # Weekly reviews & feedback
  kaggle-push/         # Kaggle API push configurations
  data/                # Local data (not tracked in git)
    raw/               # Original data (never modified)
    interim/           # Intermediate processed data
    processed/         # Analysis-ready data
    external/          # External supplementary data
```

## Data Sources

All data is freely available and redistributable:

- **SEC EDGAR** — 10-K annual reports (public domain)
- **OpenStreetMap** — Cafe/restaurant POIs via Overpass API (ODbL)
- **MTA** — NYC subway ridership (public government data)
- **US Census / ACS** — Tract-level demographics (public domain)
- **NYC PLUTO** — Building/lot attributes (public data)
- **NYC DOT** — Pedestrian counts (public data)

## Tech Stack

Python | pandas | geopandas | scikit-learn | OSMnx | Plotly | Folium | matplotlib | scipy | pyLDAvis | NetworkX

## License

Code: MIT License. Data: see individual source licenses above.
