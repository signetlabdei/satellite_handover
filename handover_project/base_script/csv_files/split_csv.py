import pandas as pd

def split_csv_by_hour(input_filename):
    print(f"Reading {input_filename}...")
    
    # Load the dataset
    df = pd.read_csv(input_filename)
    
    # Convert the 'time' column to actual datetime objects for grouping
    df['time'] = pd.to_datetime(df['time'])
    
    # Group the data into 1-hour blocks based on the 'time' column
    # '1H' stands for 1-hour frequency
    grouped = df.groupby(pd.Grouper(key='time', freq='1h'))
    
    for timestamp, group in grouped:
        # Skip empty groups if there are gaps in the time data
        if group.empty:
            continue
            
        # Format the timestamp to match your desired filename pattern (YYYY_MM_DD_HH)
        date_hour_str = timestamp.strftime("%Y_%m_%d_%H")
        
        # Construct the new filename
        output_filename = f"50km_25beams_sc9_padova_{date_hour_str}_1h.csv"
        
        # Save the group to a new CSV file without the pandas row indices
        group.to_csv(output_filename, index=False)
        print(f"Saved: {output_filename} with {len(group)} rows.")

if __name__ == "__main__":
    # Your specific input file name
    input_file = "50km_25beams_sc9_padova_2026_07_05_21_6h.csv"
    split_csv_by_hour(input_file)
    print("Splitting complete!")