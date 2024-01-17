import requests
import csv
import os
from operator import itemgetter

# Constants

COMMODITY_CODES = [
    '0440000',  # Corn
    '2231000',  # Oilseed, Copra
    '2223000',  # Oilseed, Cottonseed
    '2232000',  # Oilseed, Palm Kernel
    '2221000',  # Oilseed, Peanut
    '2226000',  # Oilseed, Rapeseed
    '2222000',  # Oilseed, Soybean
    '2224000',  # Oilseed, Sunflowerseed
    '4232000',  # Oil, Soybean
    '0813100',  # Meal, Soybean
    '0410000',  # Wheat
    '4233000',  # Oil, Cottonseed
    '4235000',  # Oil, Olive
    '4243000',  # Oil, Palm
    '4244000',  # Oil, Palm Kernel
    '4234000',  # Oil, Peanut
    '4239100',  # Oil, Rapeseed
    '4236000',  # Oil, Sunflowerseed
    '4242000',  # Oil, Coconut
    '0813700',  # Meal, Copra
    '0813300',  # Meal, Cottonseed
    '0814200',  # Meal, Fish
    '0813800',  # Meal, Palm Kernel
    '0813200',  # Meal, Peanut
    '0813600',  # Meal, Rapeseed
    '0813500',  # Meal, Sunflowerseed
]

API_ENDPOINT = "https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear"
API_KEY = '697486e5-932d-46d3-804a-388452a19d70'
# New constants for the new endpoint
WORLD_API_ENDPOINT = "https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetWorldCommodityDataByYear"

def fetch_data(commodity_code, market_year, endpoint):
    url = f"{endpoint}?commodityCode={commodity_code}&marketYear={market_year}"
    headers = {
        'Accept': 'application/json',
        'API_KEY': API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Data fetched for commodity code {commodity_code}, market year {market_year} from {endpoint}")
        return response.json()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    print(f"Returning empty list for commodity code {commodity_code}, market year {market_year}")
    return []

def parse_data(json_data, commodity_code, market_year):
   organized_data = {}
   if json_data:
       for entry in json_data:
           country = entry['CountryName'].strip()
           month = str(int(entry['Month'])) # Convert to string for consistent key handling
           attribute_description = entry['AttributeDescription'].strip()
           
           # Check if the country entry already exists
           if country not in organized_data:
               organized_data[country] = {}
           
           # Use a composite key of month and attribute to ensure uniqueness
           month_attribute_key = f"{month}-{attribute_description}"
           if month_attribute_key not in organized_data[country]:
               organized_data[country][month_attribute_key] = {'CalendarYear': entry['CalendarYear'], 'Value': entry['Value']}
           else:
               organized_data[country][month_attribute_key]['Value'] += entry['Value']

       print(f"Data organized for commodity code {commodity_code}, market year {market_year}")
   else:
       print(f"No data to organize for commodity code {commodity_code}, market year {market_year}")
   return organized_data

def create_attribute_unit_csv(json_data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['AttributeDescription', 'UnitDescription'])
        
        attribute_unit_pairs = set()
        for entry in json_data:
            attribute_description = entry['AttributeDescription'].strip()
            unit_description = entry['UnitDescription'].strip()
            attribute_unit_pairs.add((attribute_description, unit_description))
        
        for attribute, unit in sorted(attribute_unit_pairs):
            writer.writerow([attribute, unit])
            
        print(f"CSV file created for attribute-unit pairs: {filename}")


def write_to_csv(all_data, filename, all_attributes):
    headers = ['Country', 'Market Year', 'Calendar Year', 'Month']
    headers.extend(sorted(all_attributes))

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for country, year_month_data in all_data.items():
            for year_month, data in year_month_data.items():
                year, month = year_month.split('-')
                row = [country, year, data['Calendar Year'], month]
                row.extend([data['Attributes'].get(attr, '') for attr in sorted(all_attributes)])
                writer.writerow(row)





# Main Script Logic
def main():
    all_json_data = []  # List to collect all entries from both endpoints
    for commodity_code in COMMODITY_CODES:
        all_data_country = {}
        all_data_world = {}
        all_attributes = set()

        # Collect and aggregate country data
        for year in range(1960, 2023):
            json_data_country = fetch_data(commodity_code, str(year), API_ENDPOINT)
            organized_data_country = parse_data(json_data_country, commodity_code, str(year))

            # Aggregate country data
            for country, months_data in organized_data_country.items():
                if country not in all_data_country:
                    all_data_country[country] = {}
                for month_attribute_key, value in months_data.items():
                    month, attribute = month_attribute_key.split('-', 1)
                    year_month_key = f"{year}-{month}"
                    if year_month_key not in all_data_country[country]:
                        all_data_country[country][year_month_key] = {'Calendar Year': value['CalendarYear'], 'Attributes': {}}
                    all_data_country[country][year_month_key]['Attributes'][attribute] = value['Value']
                    all_attributes.add(attribute)

        # Define filenames
        filename_country = f'psd_data_{commodity_code}_country.csv'
        filename_world = f'psd_data_{commodity_code}_world.csv'

        # Write country data to CSV
        write_to_csv(all_data_country, filename_country, all_attributes)

        # Collect and aggregate world data
        for year in range(1960, 2023):
            json_data_world = fetch_data(commodity_code, str(year), WORLD_API_ENDPOINT)
            organized_data_world = parse_data(json_data_world, commodity_code, str(year))

            # Aggregate world data
            for country, months_data in organized_data_world.items():
                if country not in all_data_world:
                    all_data_world[country] = {}
                for month_attribute_key, value in months_data.items():
                    month, attribute = month_attribute_key.split('-', 1)
                    year_month_key = f"{year}-{month}"
                    if year_month_key not in all_data_world[country]:
                        all_data_world[country][year_month_key] = {'Calendar Year': value['CalendarYear'], 'Attributes': {}}
                    all_data_world[country][year_month_key]['Attributes'][attribute] = value['Value']
                    # all_attributes.add(attribute) - This line is not needed as all attributes are already added from country data aggregation

        # Write world data to CSV
        write_to_csv(all_data_world, filename_world, all_attributes)

        # Collect json_data for attribute-unit CSV creation
        all_json_data.extend(json_data_country)
        all_json_data.extend(json_data_world)

        # print(f"CSV files for commodity code {commodity_code} created: {filename_country} and {filename_world}")
        # print(f"Country data written to {os.path.abspath(filename_country)}")
        # print(f"World data written to {os.path.abspath(filename_world)}")

    # After collecting data from all commodity codes, create the attribute-unit CSV
    attribute_unit_csv_filename = 'attribute_unit_pairs.csv'
    create_attribute_unit_csv(all_json_data, attribute_unit_csv_filename)

if __name__ == "__main__":
    main()

