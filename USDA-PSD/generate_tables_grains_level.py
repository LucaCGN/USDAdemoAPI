import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

def generate_grouped_commodity_table(df, commodities_info, output_dir, filename, variable, years):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    aggregated_data = pd.DataFrame(columns=['Commodity/Category'] + years)
    row_index = 0

    for category, items in commodities_info.items():
        category_sum = pd.Series(index=years, dtype=float).fillna(0)

        for name, code in items:
            df_filtered = df[(df['Commodity Code'] == code) & (df['Country'] == 'WORLD')]
            variable_series = df_filtered.pivot_table(index='Commodity Code', columns='Market Year', values=variable, aggfunc='sum').squeeze()
            variable_series = variable_series.reindex(years).fillna(0)
            aggregated_data.loc[row_index] = [name] + variable_series.tolist()
            row_index += 1
            category_sum = category_sum.add(variable_series, fill_value=0)

        aggregated_data.loc[row_index] = [category] + category_sum.tolist()
        row_index += 1

    output_path = os.path.join(output_dir, f"{filename}-{variable[0]}.csv")
    aggregated_data.to_csv(output_path, index=False)
    print(f"Table saved as {output_path}")

# Read the consolidated data
df = read_data('consolidated_data.csv')

# Define the list of commodity codes and names for the different categories
commodities_info = {
    'OILSEEDS': [
        ('Copra', '2231000'),
        ('Cottonseed', '2223000'),
        ('Palm Kernel', '2232000'),
        ('Peanut', '2221000'),
        ('Rapeseed', '2226000'),
        ('Soybean', '2222000'),
        ('Sunflowerseed', '2224000')
    ],
    'PROTEIN MEALS': [
        ('Soybean Meal', '0813100'),
        ('Copra Meal', '0813700'),
        ('Cottonseed Meal', '0813300'),
        ('Palm Kernel Meal', '0813800'),
        ('Peanut Meal', '0813200'),
        ('Rapeseed Meal', '0813600'),
        ('Sunflowerseed Meal', '0813500'),
        ('Fish Meal', '0814200')
    ],
    'VEGETABLE OILS': [
        ('Palm Oil', '4243000'),
        ('Soybean Oil', '4232000'),
        ('Rapeseed Oil', '4239100'),
        ('Sunflowerseed Oil', '4236000'),
        ('Palm Kernel Oil', '4244000'),
        ('Peanut Oil', '4234000'),
        ('Cottonseed Oil', '4233000'),
        ('Coconut Oil', '4242000'),
        ('Olive Oil', '4235000')
    ]
}

# Define the output directory for MUNOLEA-P
output_dir_P = 'Final-Tables'
# Define the output directory for other tables
output_dir_other = 'Final-Tables/MUNODOLE'

# Define the years for which you want to gather data
years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']

# Variables to generate tables for
variables = ['Production', 'MY Exports', 'Total Supply', 'Ending Stocks']

# Generate tables for each variable
for variable in variables:
    if variable == 'Production':
        generate_grouped_commodity_table(df, commodities_info, output_dir_P, 'MUNOLEA', variable, years)
    else:
        generate_grouped_commodity_table(df, commodities_info, output_dir_other, 'MUNOLEA', variable, years)

print("All tables processed.")