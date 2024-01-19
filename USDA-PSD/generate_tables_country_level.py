import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

def generate_table(df, table_spec):
    years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

    print(f"\nGenerating table for {table_spec['filename']}...")
    print(f"Filtering for Commodity Code: {table_spec['commodity_code']}")
    
    # Filter DataFrame based on commodity code, countries, and specified years
    df_filtered = df[
        (df['Commodity Code'] == table_spec['commodity_code']) & 
        (df['Country'].isin(table_spec['countries'])) & 
        (df['Market Year'].astype(str).isin(years))
    ]
    
    # Keep columns that match the attribute description
    cols_to_keep = ['Country', 'Market Year'] + [col for col in df_filtered if table_spec['attribute_descriptions'][0] in col]
    df_filtered = df_filtered[cols_to_keep]

    # Debug: Print the DataFrame after filtering
    print(df_filtered.head())

    # Pivot the DataFrame to get years as columns and countries as rows
    table_pivot = df_filtered.pivot_table(index='Country', columns='Market Year', aggfunc='sum')

    # Define the output path and save the table
    output_path = os.path.join(table_spec['output_dir'], f"{table_spec['filename']}.csv")
    table_pivot.to_csv(output_path)
    print(f"Table saved as {output_path}")

# Read the consolidated data
df = read_data('consolidated_data.csv')


# Table specifications
table_specs = {
    'MUNEXPIMP-EX': {
        'commodity_code': '2222000', 
        'countries': ['WORLD', 'Brazil', 'United States', 'Argentina', 'Paraguay', 'Canada'], 
        'output_dir': 'Final-Tables-soy', 
        'filename': 'MUNEXPIMP-EX', 
        'attribute_descriptions': ['MY Exports']
    },
    'MUNPRO': {
        'commodity_code': '2222000', 
        'countries': ['Brazil', 'Argentina', 'Paraguay', 'Bolivia', 'Uruguay', 'United States', 'Canada', 'China', 'India', 'Russia', 'Ukraine', 'European Union', 'WORLD'], 
        'output_dir': 'Final-Tables-soy', 
        'filename': 'MUNPRO', 
        'attribute_descriptions': ['Production']
    },
    'MUNEXPIMP-IM': {
        'commodity_code': '2222000', 
        'countries': ['WORLD', 'China', 'EU', 'Mexico', 'Egypt', 'Argentina', 'Thailand', 'Japan', 'Turkey', 'Indonesia'], 
        'output_dir': 'Final-Tables-soy', 
        'filename': 'MUNEXPIMP-IM', 
        'attribute_descriptions': ['MY Imports']
    },
    # Add other table specifications here...
}

# Generate tables
for table_spec in table_specs.values():
    generate_table(df, table_spec)

print("All tables processed.")
