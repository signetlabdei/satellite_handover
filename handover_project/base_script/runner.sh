#!/bin/bash

set -e

# List the exact files you want to process in order
FILES=(
    "50km_25beams_sc9_padova_2026_07_05_18_1h.csv"
    "50km_25beams_sc9_padova_2026_07_05_19_1h.csv"
    "50km_25beams_sc9_padova_2026_07_05_20_1h.csv"
    "50km_25beams_sc9_padova_2026_07_05_21_1h.csv"
    "50km_25beams_sc9_padova_2026_07_05_22_1h.csv"
    "50km_25beams_sc9_padova_2026_07_05_23_1h.csv"
    "50km_25beams_sc9_padova_2026_07_06_00_1h.csv"
    "50km_25beams_sc9_padova_2026_07_06_01_1h.csv"
    "50km_25beams_sc9_padova_2026_07_06_02_1h.csv"
)

for df_file in "${FILES[@]}"; do
    echo "=================================================="
    echo "Starting execution for: $df_file"
    echo "=================================================="
    
    python3 main.py --df_name "$df_file"
done

echo "All timeblocks processed successfully!"