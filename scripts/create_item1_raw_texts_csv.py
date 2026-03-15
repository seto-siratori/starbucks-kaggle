"""
Create item1_raw_texts.csv from individual FY text files.

Run this script once before using notebook_f_lda_explorer.ipynb:
    python scripts/create_item1_raw_texts_csv.py
"""
import csv
import glob
import os

ITEM1_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "interim", "sec-edgar", "item1")
OUTPUT_PATHS = [
    os.path.join(os.path.dirname(__file__), "..", "data", "interim", "item1_raw_texts.csv"),
    os.path.join(os.path.dirname(__file__), "..", "dataset-upload", "nlp-corpus", "item1_raw_texts.csv"),
]


def main():
    files = sorted(glob.glob(os.path.join(ITEM1_DIR, "FY*_item1.txt")))
    if not files:
        raise FileNotFoundError(f"No FY*_item1.txt files found in {ITEM1_DIR}")

    rows = []
    for fpath in files:
        fname = os.path.basename(fpath)
        fy = int(fname.replace("FY", "").replace("_item1.txt", ""))
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        rows.append((fy, text))

    rows.sort(key=lambda x: x[0])
    print(f"Read {len(rows)} files: FY{rows[0][0]}–FY{rows[-1][0]}")

    for outpath in OUTPUT_PATHS:
        outpath = os.path.normpath(outpath)
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fiscal_year", "text"])
            for fy, text in rows:
                writer.writerow([fy, text])
        print(f"Saved: {outpath} ({os.path.getsize(outpath):,} bytes)")


if __name__ == "__main__":
    main()
