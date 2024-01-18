import pandas as pd
import os

# Function to extract commodity code from filename
def get_commodity_code(filename):
    # Assumes the format 'psd_data_<commodity_code>_...'
    return filename.split('_')[2]

# Function to read and process individual files
def process_file(filepath, master_columns):
    commodity_code = get_commodity_code(os.path.basename(filepath))
    df = pd.read_csv(filepath)
    df['Commodity Code'] = commodity_code  # Add commodity code column
    for col in master_columns:
        if col not in df.columns:
            df[col] = 0  # Initialize missing columns with zeros
    return df

# Main function to consolidate data
def consolidate_data(file_list):
    all_columns = set()
    # Identify all unique columns
    for filepath in file_list:
        df = pd.read_csv(filepath)
        all_columns.update(df.columns)

    master_columns = list(all_columns) + ['Commodity Code']
    
    # Consolidate data
    consolidated_data = pd.DataFrame(columns=master_columns)
    for filepath in file_list:
        df_processed = process_file(filepath, master_columns)
        consolidated_data = consolidated_data.append(df_processed, ignore_index=True)
    
    # Save to a new file
    consolidated_data.to_csv('consolidated_data.csv', index=False)
    print("Consolidation Complete. File saved as 'consolidated_data.csv'.")

# List of file paths to process
file_list = ['path_to_file1.csv', 'path_to_file2.csv', ...]

if __name__ == "__main__":
    consolidate_data(file_list)
