import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

# Function to generate the tables based on the specifications
def generate_table(df, commodity_code, country, attributes, years, filename_prefix):
    # Ensure the 'Final-Tables' directory exists
    output_dir = 'Final-Tables-soy'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Filter data by commodity code and country
    filtered_df = df[(df['Commodity Code'] == commodity_code) & (df['Country'].str.upper() == country.upper())]

    # Initialize empty DataFrame for results
    results_df = pd.DataFrame(index=attributes, columns=years)

    # Fill in the results DataFrame
    for year in years:
        year_data = filtered_df[filtered_df['Market Year'] == year]
        if not year_data.empty:
            for attribute in attributes:
                if attribute in year_data.columns:
                    results_df.at[attribute, year] = year_data[attribute].sum()
                else:
                    print(f"Attribute '{attribute}' not found for commodity '{commodity_code}' in year {year}.")

    # Set the index name to 'Variable/Year' before saving the CSV
    results_df.index.name = 'Variable/Year'

    # Save the results to a CSV file in the 'Final-Tables' folder
    output_file_path = os.path.join(output_dir, f"{filename_prefix}.csv")
    results_df.to_csv(output_file_path, index=True)  # index=True to include the index in the CSV
    print(f"Table saved as {output_file_path}")

# Define file paths and read the consolidated data
consolidated_data_path = 'consolidated_data.csv'
df = read_data(consolidated_data_path)

# Common specifications for attributes and years
attributes = ['Beginning Stocks', 'Production', 'MY Imports', 'Crush', 'Total Dom. Cons.', 'MY Exports', 'Ending Stocks']
years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']


# Commodity codes and countries for the groups
groups = {
    "MUNOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "WORLD"},
    "UEOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "European Union"},
    "CHIOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "China"}
}

# Generate tables
for group_name, group_info in groups.items():
    counter = 1  # Reset counter for each group
    for commodity_code in group_info["commodity_codes"]:
        filename_prefix = f"{group_name}-{counter}"
        generate_table(df, commodity_code, group_info["country"], attributes, years, filename_prefix)
        counter += 1  # Increment the counter for the next file in the same group

print("All tables processed.")

