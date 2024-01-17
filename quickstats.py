import requests

def fetch_corn_data(api_key, category, data_item, years):
    base_url = 'https://quickstats.nass.usda.gov/api/api_GET/'
    for year in years:
        params = {
            'key': api_key,
            'sector_desc': 'CROPS',
            'group_desc': 'FIELD CROPS',
            'commodity_desc': 'CORN',
            'statisticcat_desc': category,
            'short_desc': data_item,
            'agg_level_desc': 'STATE',  # Geographic level set to STATE
            'year': year,  # Query for each year individually
            'format': 'csv'
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            filename = f"corn_{category.lower().replace(' ', '_')}_{year}.csv"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Data for {year} has been successfully saved to {filename}")
        else:
            # Handle errors
            print(f"Failed to fetch data for {year}: {response.status_code} - {response.text}")

# Usage example for multiple years
api_key = '1E0BC2ED-A9F9-367F-9AAA-5613BFF76DD5'
category = 'YIELD'
data_item = 'CORN, GRAIN - YIELD, MEASURED IN BU / ACRE'
years = ['2022', '2023', '2024']
fetch_corn_data(api_key, category, data_item, years)
