import pandas as pd
import os

def read_data(file_path):
    print(f"Reading data from {file_path}...")
    # Make sure this is inside the same block where you're going to use 'df'
    return pd.read_csv(file_path, dtype={'Commodity Code': str, 'Market Year': str})

def generate_table(df, table_spec):
    years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
    print(f"\nGenerating table for {table_spec['filename']}...")
    
    # Filter DataFrame based on commodity code, countries, and specified years
    df_filtered = df[
        (df['Commodity Code'] == table_spec['commodity_code']) & 
        (df['Country'].isin(table_spec['countries'])) & 
        (df['Market Year'].astype(str).isin(years))
    ]
    
    # Keep columns that match the attribute description
    cols_to_keep = ['Country', 'Market Year'] + [col for col in df.columns if table_spec['attribute_descriptions'][0] in col]
    df_filtered = df_filtered[cols_to_keep]

    # Debug: Print the DataFrame after filtering
    print(df_filtered.head())

    # Pivot the DataFrame to get years as columns and countries as rows
    table_pivot = df_filtered.pivot_table(index='Country', columns='Market Year', values=table_spec['attribute_descriptions'][0], aggfunc='sum')
    
    # Reset the index to turn the 'Country' index into a column
    table_pivot.reset_index(inplace=True)
    
    # Remove rows where 'Country' is empty or NaN
    table_pivot = table_pivot[table_pivot['Country'].notna() & (table_pivot['Country'] != '')]

    # Define the output path and save the table
    output_path = os.path.join(table_spec['output_dir'], f"{table_spec['filename']}.csv")
    table_pivot.to_csv(output_path, index=False)  # Set index=False to avoid writing row numbers
    print(f"Table saved as {output_path}")

# Make sure this is inside the same block where you're going to use 'df'
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
    'MUNPROMILHO': {
        'commodity_code': '0440000',
        'countries': ['USA', 'China', 'Brazil', 'EU', 'Argentina', 'Ukraine', 'Mexico', 'India', 'South Africa', 'Russia', 'Canada', 'Indonesia', 'Philippines', 'Others', 'World'],
        'output_dir': 'Final-Tables-corn',
        'filename': 'MUNPROMILHO',
        'attribute_descriptions': ['Production']
    },
    'MUNPROTRIGO': {
        'commodity_code': '0410000',
        'countries': ['EU', 'China', 'India', 'USA', 'Russia', 'Canada', 'Australia', 'Pakistan', 'Ukraine', 'Turkey', 'Iran', 'Kazakhstan', 'Argentina', 'Brazil', 'Others', 'Total'],
        'output_dir': 'Final-Tables-wheat',
        'filename': 'MUNPROTRIGO',
        'attribute_descriptions': ['Production']
    },    
    'MUNEXPIMPTRIGO-EX': {
        'commodity_code': '0410000',
        'countries': ['World', 'Russia', 'USA', 'EU', 'Canada', 'Australia', 'Ukraine', 'Argentina', 'Kazakhstan', 'Turkey', 'India', 'Others'],
        'output_dir': 'Final-Tables-wheat',
        'filename': 'MUNEXPIMPTRIGO-EX',
        'attribute_descriptions': ['TY Exports']
    },
    'MUNEXPIMPTRIGO-IM': {
        'commodity_code': '0410000',
        'countries': ['World', 'Egypt', 'Indonesia', 'China', 'Turkey', 'Philippines', 'Algeria', 'Brazil', 'Bangladesh', 'Morocco', 'EU', 'Others'],
        'output_dir': 'Final-Tables-wheat',
        'filename': 'MUNEXPIMPTRIGO-IM',
        'attribute_descriptions': ['TY Imports']
    },
    'MUNEXPIMPMILHO-EX': {
        'commodity_code': '0440000',
        'countries': ['World', 'USA', 'Brazil', 'Argentina', 'Ukraine', 'Russia', 'South Africa', 'EU', 'Paraguay', 'Others'],
        'output_dir': 'Final-Tables-corn',
        'filename': 'MUNEXPIMPMILHO-EX',
        'attribute_descriptions': ['TY Exports']
    },
    'MUNEXPIMPMILHO-IM': {
        'commodity_code': '0440000',
        'countries': ['World', 'EU', 'Mexico', 'China', 'Japan', 'Vietnam', 'South Korea', 'Egypt', 'Iran', 'Colombia', 'Algeria', 'Saudi Arabia', 'Others'],
        'output_dir': 'Final-Tables-corn',
        'filename': 'MUNEXPIMPMILHO-IM',
        'attribute_descriptions': ['TY Imports']
    }

}

# Generate tables
for table_spec in table_specs.values():
    generate_table(df, table_spec)

print("All tables processed.")
