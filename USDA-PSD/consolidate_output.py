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
    dataframes = []  # List to store individual dataframes

    # Identify all unique columns
    for filepath in file_list:
        df = pd.read_csv(filepath)
        all_columns.update(df.columns)

    master_columns = list(all_columns) + ['Commodity Code']
    
    # Process and collect data frames
    for filepath in file_list:
        df_processed = process_file(filepath, master_columns)
        dataframes.append(df_processed)
    
    # Concatenate all data frames
    consolidated_data = pd.concat(dataframes, ignore_index=True)
    
    # Save to a new file
    consolidated_data.to_csv('consolidated_data.csv', index=False)
    print("Consolidation Complete. File saved as 'consolidated_data.csv'.")


# List of file paths to process
file_list = [
    'psd_data_0410000_country.csv',
    'psd_data_0410000_world.csv',
    'psd_data_0440000_country.csv',
    'psd_data_0440000_world.csv',
    'psd_data_0813100_country.csv',
    'psd_data_0813100_world.csv',
    'psd_data_0813200_country.csv',
    'psd_data_0813200_world.csv',
    'psd_data_0813300_country.csv',
    'psd_data_0813300_world.csv',
    'psd_data_0813500_country.csv',
    'psd_data_0813500_world.csv',
    'psd_data_0813600_country.csv',
    'psd_data_0813600_world.csv',
    'psd_data_0813700_country.csv',
    'psd_data_0813700_world.csv',
    'psd_data_0813800_country.csv',
    'psd_data_0813800_world.csv',
    'psd_data_0814200_country.csv',
    'psd_data_0814200_world.csv',
    'psd_data_2221000_country.csv',
    'psd_data_2221000_world.csv',
    'psd_data_2222000_country.csv',
    'psd_data_2222000_world.csv',
    'psd_data_2223000_country.csv',
    'psd_data_2223000_world.csv',
    'psd_data_2224000_country.csv',
    'psd_data_2224000_world.csv',
    'psd_data_2226000_country.csv',
    'psd_data_2226000_world.csv',
    'psd_data_2231000_country.csv',
    'psd_data_2231000_world.csv',
    'psd_data_2232000_country.csv',
    'psd_data_2232000_world.csv',
    'psd_data_4232000_country.csv',
    'psd_data_4232000_world.csv',
    'psd_data_4233000_country.csv',
    'psd_data_4233000_world.csv',
    'psd_data_4234000_country.csv',
    'psd_data_4234000_world.csv',
    'psd_data_4235000_country.csv',
    'psd_data_4235000_world.csv',
    'psd_data_4236000_country.csv',
    'psd_data_4236000_world.csv',
    'psd_data_4239100_country.csv',
    'psd_data_4239100_world.csv',
    'psd_data_4242000_country.csv',
    'psd_data_4242000_world.csv',
    'psd_data_4243000_country.csv',
    'psd_data_4243000_world.csv',
    'psd_data_4244000_country.csv',
    'psd_data_4244000_world.csv'
]


if __name__ == "__main__":
    consolidate_data(file_list)
