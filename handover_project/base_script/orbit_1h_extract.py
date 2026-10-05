import pandas as pd
import os
import re

# ==========================================
#               CONFIGURATION
# ==========================================
# Write your exact input file name here:
INPUT_FILE = "200km_25beams_sc9_padova_2026_07_06_12_6h.csv"

# Which hour would you like to extract? 
# (1 = first hour, 2 = second hour, etc.)
HOUR_TO_EXTRACT = 6  
# ==========================================

def main():
    # Check if the file exists
    if not os.path.isfile(INPUT_FILE):
        print(f"Error: The file '{INPUT_FILE}' was not found in the current directory.")
        return

    if HOUR_TO_EXTRACT < 1:
        print("Error: HOUR_TO_EXTRACT must be 1 or greater.")
        return

    try:
        print(f"Processing '{INPUT_FILE}' for hour {HOUR_TO_EXTRACT}...")
        
        # Read the CSV file
        df = pd.read_csv(INPUT_FILE)
        
        # Identify the second column (index 1)
        time_col = df.columns[1]

        # Convert to datetime objects
        df[time_col] = pd.to_datetime(df[time_col], errors='coerce')

        # Determine the specific time window based on the chosen hour
        earliest_time = df[time_col].min()
        window_start = earliest_time + pd.Timedelta(hours=HOUR_TO_EXTRACT - 1)
        window_end = earliest_time + pd.Timedelta(hours=HOUR_TO_EXTRACT)

        # Filter the DataFrame for the selected 1-hour block
        subset_df = df[(df[time_col] >= window_start) & (df[time_col] < window_end)]

        if subset_df.empty:
            print(f"\nWarning: No data found for hour {HOUR_TO_EXTRACT}.")
            print(f"The dataset only goes up to {df[time_col].max()}.")
            return

        # Construct the dynamic output filename
        # This regex looks for: (Any Prefix)_(YYYY_MM_DD_HH)_(Duration)h.csv
        pattern = r"^(.*?)_\d{4}_\d{2}_\d{2}_\d{2}_\d+h\.csv$"
        match = re.match(pattern, INPUT_FILE)
        
        # Format the actual starting date of the subset into YYYY_MM_DD_HH
        new_date_str = window_start.strftime("%Y_%m_%d_%H")

        if match:
            # Rebuild the string: Prefix + New Date + 1h.csv
            prefix = match.group(1) 
            output_file = f"{prefix}_{new_date_str}_1h.csv"
        else:
            # Fallback just in case a filename is used without the exact suffix format
            output_file = f"extracted_data_{new_date_str}_1h.csv"

        # Save the subset to a new CSV
        subset_df.to_csv(output_file, index=False)

        print("\nSuccess!")
        print(f"Extracted {len(subset_df)} rows for hour {HOUR_TO_EXTRACT}.")
        print(f"Time window: {window_start} to {window_end}")
        print(f"Saved subset to: {output_file}")

    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    main()