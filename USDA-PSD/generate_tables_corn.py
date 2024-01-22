import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

def generate_corn_table(df, commodity_code, country, attributes, years, filename):
    output_dir = 'Final-Tables-corn'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, f"{filename}.csv")

    filtered_df = df[(df['Commodity Code'] == commodity_code) & (df['Country'].str.upper() == country.upper())]

    results_df = pd.DataFrame(index=attributes, columns=years)
    
    for year in years:
        year_data = filtered_df[filtered_df['Market Year'] == year]
        for attribute in attributes:
            if attribute in year_data.columns:
                if attribute == 'Yield':  # Handle conversion for Yield if necessary
                    results_df.at[attribute, year] = (year_data[attribute] * 67.25).sum()
                else:
                    results_df.at[attribute, year] = year_data[attribute].sum()

    results_df.index.name = 'Variable/Year'
    results_df.to_csv(output_file_path, index=True)
    print(f"Table saved as {output_file_path}")

df = read_data('consolidated_data.csv')

corn_attributes = ['Beginning Stocks', 'Production', 'Area Harvested', 'MY Imports', 'Total Supply',
                    'Total Consumption', 'Feed and Residual', 'FSI Consumption', 'MY Exports', 'Yield', 'Ending Stocks']
corn_years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']
corn_code = "0440000"
corn_countries = {
    "MUNODMILHO": "World",
    "ARGODMILHO": "Argentina"
}

for filename, country in corn_countries.items():
    generate_corn_table(df, corn_code, country, corn_attributes, corn_years, filename)

print("Corn tables generated.")
