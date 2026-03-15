"""
Build stores_enriched.csv: 171 Starbucks × ~30 columns.

Join 1: MapPLUTO (nearest neighbor) → building attributes
Join 2: MTA stations (nearest neighbor) → station name, distance, ridership
Join 3: Competitor density → counts within 250m/500m/1000m
"""

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from pathlib import Path

# --- Constants ---
# Simple planar projection for Manhattan (error <0.5%)
REF_LAT = 40.75
M_PER_DEG_LAT = 111_320
M_PER_DEG_LON = M_PER_DEG_LAT * np.cos(np.radians(REF_LAT))

DATA_DIR = Path("data")


def to_meters(lat, lon):
    """Convert lat/lon arrays to approximate meter coordinates."""
    return lat * M_PER_DEG_LAT, lon * M_PER_DEG_LON


def main():
    # =========================================================
    # Load base table
    # =========================================================
    sbux = pd.read_csv(DATA_DIR / "processed/manhattan_starbucks_osm.csv")
    print(f"Base: {sbux.shape[0]} Starbucks stores, {sbux.shape[1]} columns")
    assert sbux.shape[0] == 171, f"Expected 171 rows, got {sbux.shape[0]}"

    # =========================================================
    # JOIN 1: MapPLUTO → building attributes (nearest neighbor)
    # =========================================================
    print("\n--- Join 1: MapPLUTO ---")
    pluto_cols = ["lat", "lon", "bbl", "landuse", "bldgclass", "numfloors",
                  "yearbuilt", "unitstotal", "retailarea", "assesstot",
                  "comarea", "lotarea", "zonedist1"]
    pluto = pd.read_csv(DATA_DIR / "raw/pluto_manhattan.csv", usecols=pluto_cols)
    pluto = pluto.dropna(subset=["lat", "lon"])
    print(f"  PLUTO lots with coords: {len(pluto)}")

    # Build KDTree in meter space
    sbux_y, sbux_x = to_meters(sbux["lat"].values, sbux["lon"].values)
    pluto_y, pluto_x = to_meters(pluto["lat"].values, pluto["lon"].values)

    tree_pluto = cKDTree(np.column_stack([pluto_x, pluto_y]))
    dists, idxs = tree_pluto.query(np.column_stack([sbux_x, sbux_y]), k=1)

    # Attach PLUTO columns
    pluto_match = pluto.iloc[idxs].reset_index(drop=True)
    for col in ["bbl", "landuse", "bldgclass", "numfloors", "yearbuilt",
                "unitstotal", "retailarea", "assesstot", "comarea",
                "lotarea", "zonedist1"]:
        sbux[f"pluto_{col}"] = pluto_match[col].values
    sbux["pluto_dist_m"] = dists

    # Sanity checks
    assert sbux.shape[0] == 171, f"Row count changed: {sbux.shape[0]}"
    assert (sbux["pluto_dist_m"] <= 100).all(), \
        f"PLUTO match >100m: max={sbux['pluto_dist_m'].max():.1f}m"
    pct_commercial = sbux["pluto_landuse"].isin(["04", "05", 4, 5]).mean()
    print(f"  Max match distance: {sbux['pluto_dist_m'].max():.1f}m")
    print(f"  Median match distance: {sbux['pluto_dist_m'].median():.1f}m")
    print(f"  Commercial/Mixed land use: {pct_commercial:.1%}")
    print(f"  NULL counts: {sbux[[c for c in sbux.columns if c.startswith('pluto_')]].isnull().sum().to_dict()}")

    # =========================================================
    # JOIN 2: MTA nearest station
    # =========================================================
    print("\n--- Join 2: MTA nearest station ---")
    mta = pd.read_csv(DATA_DIR / "processed/manhattan_mta_ridership_summary.csv")
    print(f"  MTA stations: {len(mta)}")

    mta_y, mta_x = to_meters(mta["lat"].values, mta["lon"].values)
    tree_mta = cKDTree(np.column_stack([mta_x, mta_y]))
    dists_mta, idxs_mta = tree_mta.query(np.column_stack([sbux_x, sbux_y]), k=1)

    mta_match = mta.iloc[idxs_mta].reset_index(drop=True)
    sbux["mta_station_id"] = mta_match["station_complex_id"].values
    sbux["mta_station_name"] = mta_match["station_name"].values
    sbux["mta_dist_m"] = dists_mta
    sbux["mta_avg_daily_ridership"] = mta_match["avg_daily_ridership"].values

    # Sanity checks
    assert sbux.shape[0] == 171, f"Row count changed: {sbux.shape[0]}"
    print(f"  Max station distance: {sbux['mta_dist_m'].max():.0f}m")
    print(f"  Median station distance: {sbux['mta_dist_m'].median():.0f}m")
    print(f"  Within 500m: {(sbux['mta_dist_m'] <= 500).sum()}/171 "
          f"({(sbux['mta_dist_m'] <= 500).mean():.1%})")
    print(f"  NULL counts: {sbux[['mta_station_id','mta_station_name','mta_avg_daily_ridership']].isnull().sum().to_dict()}")

    # =========================================================
    # JOIN 3: Competitor density (250m / 500m / 1000m)
    # =========================================================
    print("\n--- Join 3: Competitor density ---")
    cafes = pd.read_csv(DATA_DIR / "processed/manhattan_cafes_osm.csv")

    # Split by brand category (exclude starbucks from competitors)
    cafes = cafes[cafes["brand_category"] != "starbucks"]
    dunkin = cafes[cafes["brand_category"] == "dunkin"].copy()
    others = cafes[cafes["brand_category"].isin(["independent", "branded"])].copy()
    print(f"  Dunkin': {len(dunkin)}, Other cafes: {len(others)}")

    # Starbucks self-cannibalization: use sbux itself (k=2 to skip self)
    tree_sbux = cKDTree(np.column_stack([sbux_x, sbux_y]))

    # Dunkin' tree
    dunk_y, dunk_x = to_meters(dunkin["lat"].values, dunkin["lon"].values)
    tree_dunk = cKDTree(np.column_stack([dunk_x, dunk_y]))

    # Other cafes tree
    oth_y, oth_x = to_meters(others["lat"].values, others["lon"].values)
    tree_oth = cKDTree(np.column_stack([oth_x, oth_y]))

    sbux_coords = np.column_stack([sbux_x, sbux_y])

    for radius in [250, 500, 1000]:
        # Starbucks within radius (excluding self)
        sbux_counts = tree_sbux.query_ball_point(sbux_coords, r=radius)
        sbux[f"n_starbucks_{radius}m"] = [len(c) - 1 for c in sbux_counts]  # -1 for self

        # Dunkin' within radius
        dunk_counts = tree_dunk.query_ball_point(sbux_coords, r=radius)
        sbux[f"n_dunkin_{radius}m"] = [len(c) for c in dunk_counts]

        # Other cafes within radius
        oth_counts = tree_oth.query_ball_point(sbux_coords, r=radius)
        sbux[f"n_other_cafe_{radius}m"] = [len(c) for c in oth_counts]

    # Nearest competitor (any cafe) distance
    all_comp_y, all_comp_x = to_meters(cafes["lat"].values, cafes["lon"].values)
    tree_all = cKDTree(np.column_stack([all_comp_x, all_comp_y]))
    nearest_comp_dist, _ = tree_all.query(sbux_coords, k=1)
    sbux["nearest_competitor_dist_m"] = nearest_comp_dist

    # Nearest other Starbucks distance (k=2, skip self)
    nearest_sbux_dist, _ = tree_sbux.query(sbux_coords, k=2)
    sbux["nearest_starbucks_dist_m"] = nearest_sbux_dist[:, 1]  # 2nd nearest = nearest other

    # Sanity checks
    assert sbux.shape[0] == 171, f"Row count changed: {sbux.shape[0]}"
    assert (sbux["n_starbucks_250m"] >= 0).all(), "Negative starbucks count"
    print(f"  Avg Starbucks within 250m: {sbux['n_starbucks_250m'].mean():.1f}")
    print(f"  Avg Starbucks within 500m: {sbux['n_starbucks_500m'].mean():.1f}")
    print(f"  Avg Dunkin' within 500m: {sbux['n_dunkin_500m'].mean():.1f}")
    print(f"  Avg other cafes within 500m: {sbux['n_other_cafe_500m'].mean():.1f}")
    print(f"  Nearest competitor: median={sbux['nearest_competitor_dist_m'].median():.0f}m, "
          f"max={sbux['nearest_competitor_dist_m'].max():.0f}m")
    print(f"  Nearest Starbucks: median={sbux['nearest_starbucks_dist_m'].median():.0f}m, "
          f"max={sbux['nearest_starbucks_dist_m'].max():.0f}m")

    # =========================================================
    # Save
    # =========================================================
    out_path = DATA_DIR / "processed/stores_enriched_v1.csv"
    sbux.to_csv(out_path, index=False)
    print(f"\n{'='*60}")
    print(f"Saved: {out_path}")
    print(f"Shape: {sbux.shape[0]} rows × {sbux.shape[1]} columns")
    print(f"Columns ({sbux.shape[1]}):")
    for i, col in enumerate(sbux.columns):
        null_count = sbux[col].isnull().sum()
        null_str = f" (NULL: {null_count})" if null_count > 0 else ""
        print(f"  {i+1:2d}. {col}{null_str}")


if __name__ == "__main__":
    main()
