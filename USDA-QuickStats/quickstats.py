import requests

def fetch_corn_data(api_key, categories_with_items, years):
    base_url = 'https://quickstats.nass.usda.gov/api/api_GET/'
    for category, data_item in categories_with_items.items():
        for year in years:
            params = {
                'key': api_key,
                'sector_desc': 'CROPS',
                'group_desc': 'FIELD CROPS',
                'commodity_desc': 'CORN',
                'statisticcat_desc': category,
                'short_desc': data_item,
                'agg_level_desc': 'STATE',  # Geographic level set to STATE
                'year': year,
                'format': 'csv'
            }
            
            response = requests.get(base_url, params=params)
            
            if response.status_code == 200:
                filename = f"corn_{data_item.lower().replace(' ', '_').replace(',', '').replace('/', '_').replace('-', '_')}_{year}.csv"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Data for {year} and category '{category}' has been successfully saved to {filename}")
            else:
                # Handle errors
                print(f"Failed to fetch data for {year} and category '{category}': {response.status_code} - {response.text}")

# Usage example for multiple years and categories
api_key = '1E0BC2ED-A9F9-367F-9AAA-5613BFF76DD5'
categories_with_items = {
    'YIELD': 'CORN, GRAIN - YIELD, MEASURED IN BU / ACRE',
    'PRODUCTION': 'CORN, GRAIN - PRODUCTION, MEASURED IN $',
    'AREA HARVESTED': 'CORN - ACRES HARVESTED',
    'AREA PLANTED': 'CORN - ACRES PLANTED'
}
years = ['2022', '2023',]
fetch_corn_data(api_key, categories_with_items, years)
