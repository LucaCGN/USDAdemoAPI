import csv
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

# Function to load variable details from CSV
def load_variable_details(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Assuming the correct CSV header is 'Column1.id'
        return {row['Column1.id']: row for row in reader}

# Function to fetch variable options for parameters
def fetch_variable_options(filename="data/arms-all-variables-december-2023.csv"):
    """
    Fetches variable options from the CSV file and formats them for use in the application.
    
    :param filename: The path to the CSV file containing variable details.
    :return: A dictionary with variable IDs as keys and variable names as values.
    """
    variable_options = {}

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            variable_id = row.get('Column1.id')
            variable_name = row.get('Column1.name')
            if variable_id and variable_name:
                variable_options[variable_id] = variable_name

    return variable_options

# Function to test the /arms/variable endpoint with parameters
def test_variable_endpoint(variable_id, variables_info, variable_options):
    variable_info = variables_info.get(variable_id, {'Column1.name': 'Unknown', 'Column1.description': ''})
    variable_name = variable_info['Column1.name']
    variable_desc = variable_info['Column1.description']
    print(f"\nTesting /arms/variable Endpoint for Variable: {variable_name} - {variable_desc}")

    try:
        response = requests.get(f"{Config.BASE_URL}/variable?api_key={Config.API_KEY}&id={variable_id}")
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, f"data/storage/variable_{variable_id}_data.csv")
        browser_url = generate_browser_url(Config.BASE_URL, f"/variable?id={variable_id}", Config.API_KEY)
        print(f"Browser URL: {browser_url}")

        if isinstance(data, dict):
            print(data)
        elif isinstance(data, list):
            print(data)
    except requests.RequestException as e:
        print(f"Error fetching data for variable {variable_name}: {e}")
