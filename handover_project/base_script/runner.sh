#!/bin/bash

set -e

# List the exact files you want to process in order
FILES=(
    "50km_25beams_sc9_padova_2026_07_05_18_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_05_19_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_05_20_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_05_21_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_05_22_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_05_23_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_00_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_01_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_02_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_03_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_04_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_05_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_06_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_07_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_08_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_09_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_10_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_11_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_12_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_13_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_14_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_15_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_16_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_17_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_18_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_19_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_20_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_21_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_22_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_06_23_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_00_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_01_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_02_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_03_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_04_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_05_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_06_1h.csv"
    # "50km_25beams_sc9_padova_2026_07_07_07_1h.csv"
)

for df_file in "${FILES[@]}"; do
    echo "=================================================="
    echo "Starting execution for: $df_file"
    echo "=================================================="
    
    python3 main.py --df_name "$df_file"
done

echo "All timeblocks processed successfully!"