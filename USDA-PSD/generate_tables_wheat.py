import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

def generate_wheat_table(df, commodity_code, country, attributes, years, filename):
    output_dir = 'Final-Tables-wheat'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, f"{filename}.csv")

    filtered_df = df[(df['Commodity Code'] == commodity_code) & (df['Country'].str.upper() == country.upper())]

    # Create an empty DataFrame with the required attributes as index and years as columns
    results_df = pd.DataFrame(index=attributes, columns=years)
    
    # Fill in the results DataFrame
    for year in years:
        year_data = filtered_df[filtered_df['Market Year'] == year]
        for attribute in attributes:
            if attribute in year_data.columns:
                results_df.at[attribute, year] = year_data[attribute].sum()

    # Set the placeholder for the first column header
    results_df.index.name = 'Variable/Year'

    # Save the results to a CSV file in the 'Final-Tables-wheat' folder
    results_df.to_csv(output_file_path, index=True)
    print(f"Table saved as {output_file_path}")


df = read_data('consolidated_data.csv')

wheat_attributes = ['Beginning Stocks', 'Production', 'Area Harvested', 'MY Imports', 'Total Supply',
                    'Total Consumption', 'Feed and Residual', 'FSI Consumption', 'Yield', 'MY Exports', 'Ending Stocks']
wheat_years = ["2021", "2022", "2023"]
wheat_code = "0410000"
wheat_countries = {
    "CHIODTRIGO": "China",
    "RUSODTRIGO": "Russia",
    "INDODTRIGO": "India",
    "MUNODTRIGO": "World",
    "UENODTRIGO": "European Union"
}

# Generate wheat tables
for filename, country in wheat_countries.items():
    generate_wheat_table(df, wheat_code, country, wheat_attributes, wheat_years, filename)

print("Wheat tables generated.")
