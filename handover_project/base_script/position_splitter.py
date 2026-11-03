#!/usr/bin/env python3
"""
Split a satellite-visibility CSV into one-hour CSV files.

Input columns (as in the example file):
    cluster_id,time,sat_name,sat_lat,sat_lon,sat_height,occurrence_countdown

Output naming keeps the original prefix and replaces the "start time + duration"
tail of the name. Example:

    50km_4beams_sc9_padova_2026_07_05_00_24h.csv
        -> 50km_4beams_sc9_padova_2026_07_05_00_1h.csv
           50km_4beams_sc9_padova_2026_07_05_01_1h.csv
           ...
           50km_4beams_sc9_padova_2026_07_05_23_1h.csv

The tail has the form  _YYYY_MM_DD_HH_<N>h  . If the input name does not end
with it, the whole stem is used as prefix. The date and hour of each output file
come from the data itself (the "time" column), so files that cross midnight are
handled correctly.

Values are copied as text, so numbers are not reformatted.

Usage:
    1) Set INPUT_FILE below and run:  python split_hourly.py
    2) Or pass the file(s) on the command line (this overrides INPUT_FILE):
           python split_hourly.py INPUT.csv [INPUT2.csv ...] [-o OUTDIR]
"""
import argparse
import re
import sys
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# EDIT HERE: name (or full path) of the file to split.
# ---------------------------------------------------------------------------
INPUT_FILE = "50km_25beams_sc9_padova_2026_07_07_15_6h.csv"

# Folder for the output files. None = same folder as the input file.
OUTPUT_DIR = None

TAIL_RE = re.compile(r"^(?P<prefix>.*?)_\d{4}_\d{2}_\d{2}_\d{2}_\d+h$")


def output_prefix(stem: str) -> str:
    """Original name without the '_YYYY_MM_DD_HH_<N>h' tail."""
    m = TAIL_RE.match(stem)
    return m.group("prefix") if m else stem


def split_file(path: Path, outdir: Path) -> list[Path]:
    # Read everything as text to keep the original number formatting.
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "time" not in df.columns:
        raise ValueError(f"{path}: no 'time' column (found: {list(df.columns)})")

    t = pd.to_datetime(df["time"])
    hour_start = t.dt.floor("h")

    prefix = output_prefix(path.stem)
    outdir.mkdir(parents=True, exist_ok=True)

    written = []
    for hs, chunk in df.groupby(hour_start, sort=True):
        name = f"{prefix}_{hs:%Y_%m_%d_%H}_1h.csv"
        out = outdir / name
        chunk.to_csv(out, index=False)
        written.append(out)
        print(f"{name}: {len(chunk)} rows  "
              f"[{chunk['time'].iloc[0]} -> {chunk['time'].iloc[-1]}]")
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="*", type=Path,
                    help="input CSV file(s); default: INPUT_FILE set in the script")
    ap.add_argument("-o", "--outdir", type=Path, default=None,
                    help="output folder (default: OUTPUT_DIR, else the input's folder)")
    args = ap.parse_args()

    inputs = args.inputs or [Path(INPUT_FILE)]
    outdir_cfg = args.outdir if args.outdir is not None else (
        Path(OUTPUT_DIR) if OUTPUT_DIR else None)

    for p in inputs:
        if not p.is_file():
            print(f"ERROR: file not found: {p}", file=sys.stderr)
            return 1
        outdir = outdir_cfg if outdir_cfg is not None else p.parent
        print(f"== {p}")
        split_file(p, outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())