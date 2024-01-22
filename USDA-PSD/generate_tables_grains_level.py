import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})


def generate_grouped_commodity_table(df, commodities_info, output_dir, filename, years):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a DataFrame to store the aggregated production data
    aggregated_data = pd.DataFrame(columns=['Commodity/Category'] + years)

    # Track the row index for where to insert data
    row_index = 0

    # Group commodities by category and calculate the production sum for each category
    for category, items in commodities_info.items():
        category_sum = pd.Series(index=years, dtype=float).fillna(0)

        for name, code in items:
            df_filtered = df[(df['Commodity Code'] == code) & (df['Country'] == 'WORLD')]
            production_series = df_filtered.pivot_table(index='Commodity Code', columns='Market Year', values='Production', aggfunc='sum').squeeze()

            # Align the series with the years, filling missing years with 0
            production_series = production_series.reindex(years).fillna(0)

            # Add the individual commodity production data to the DataFrame
            aggregated_data.loc[row_index] = [name] + production_series.tolist()
            row_index += 1  # Increment the row index for the next entry

            # Sum the production values for the category
            category_sum = category_sum.add(production_series, fill_value=0)

        # Add the category sum to the DataFrame
        aggregated_data.loc[row_index] = [category] + category_sum.tolist()
        row_index += 1  # Increment the row index for the next entry

    # Save the aggregated data to a CSV file
    output_path = os.path.join(output_dir, f"{filename}.csv")
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

# Define the output directory and filename
output_dir = 'Final-Tables'  # Or any other directory you want to use
filename = 'MUNOLEA'

# Define the years for which you want to gather data
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Generate the table
generate_grouped_commodity_table(df, commodities_info, output_dir, filename, years)

print("All tables processed.")
