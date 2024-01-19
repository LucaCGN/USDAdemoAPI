import pandas as pd
import os

# Function to read the CSV and ensure the 'Commodity Code' is read as a string
def read_data(file_path):
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

# Function to generate the tables based on the specifications
def generate_table(df, commodity_code, country, attributes, years, filename_prefix):
    # Ensure the 'Final-Tables' directory exists
    output_dir = 'Final-Tables-soy'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate tables for each of the three sets
    for i in range(1, 4):
        filename = f"{filename_prefix}-{i}.csv"
        output_file_path = os.path.join(output_dir, filename)

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
        results_df.to_csv(output_file_path, index=True)  # index=True to include the index in the CSV
        print(f"Table saved as {output_file_path}")

# Define file paths
consolidated_data_path = 'consolidated_data.csv'

# Read the consolidated data
df = read_data(consolidated_data_path)

# Common specifications
attributes = ['Beginning Stocks', 'Production', 'MY Imports', 'Crush', 'Total Dom. Cons.', 'MY Exports', 'Ending Stocks']
years = ["2021", "2022", "2023"]

# Commodity codes and countries for the three groups
groups = {
    "MUNOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "WORLD"},
    "UEOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "European Union"},
    "CHIOD": {"commodity_codes": ["2222000", "0813100", "4232000"], "country": "China"}
}

# Generate tables for each group
for group_name, group_info in groups.items():
    for commodity_code in group_info["commodity_codes"]:
        generate_table(df, commodity_code, group_info["country"], attributes, years, group_name)

print("All tables processed.")
