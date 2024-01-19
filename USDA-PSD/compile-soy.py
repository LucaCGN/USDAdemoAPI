import pandas as pd
import os

# Function to compile and format tables for Excel consumption
def compile_and_format_tables(tables, group_name, country_name):
    # Read the tables into DataFrames
    dataframes = [pd.read_csv(table) for table in tables]

    # Combine the dataframes laterally, reset index to avoid the unnamed column when saving to CSV
    combined_df = pd.concat(dataframes, axis=1).reset_index(drop=True)

    # Prepare title rows based on group name and country
    title_rows = [[''] * combined_df.shape[1]]  # Empty row for spacing
    title_rows.append([f"{country_name} - {commodity} SUPPLY & DEMAND" for commodity in commodities])

    # Add commodity code row
    title_rows.append([f"Commodity Code: {code}" for code in group_info['commodity_codes']] + [''] * (combined_df.shape[1] - 3))

    # Add the title rows to the top of the DataFrame
    title_df = pd.DataFrame(title_rows, columns=combined_df.columns)
    final_df = pd.concat([title_df, combined_df], ignore_index=True)

    return final_df

# Define the directory where the individual tables are located
base_dir = 'Final-Tables'

# Define the output directory for the compiled tables
output_dir = 'Compiled-Tables'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Group specifications with commodity codes and country names
groups = {
    "MUNOD": {"commodity_codes": ["0813100", "0813200", "0813300"], "country": "World"},
    "UEOD": {"commodity_codes": ["0410000", "0420000", "0430000"], "country": "EU"},
    "CHIOD": {"commodity_codes": ["0110000", "0120000", "0130000"], "country": "China"}
}

# Compile tables for each group
for group_name, group_info in groups.items():
    # Define the paths to the individual tables
    tables = [os.path.join(base_dir, f"{group_name}-{i}.csv") for i in range(1, 4)]
    
    # Compile and format the tables
    compiled_df = compile_and_format_tables(tables, group_name, group_info['country'], group_info['commodity_codes'])
    
    
    # Save the compiled table to a CSV file
    output_filename = os.path.join(output_dir, f"{group_name}_compiled.csv")
    compiled_df.to_csv(output_filename, index=False)
    print(f"Compiled table for {group_name} saved to {output_filename}")

print("All tables have been compiled and saved.")
