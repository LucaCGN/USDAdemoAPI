## modules/state.py
```
# state.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def get_state_options():
    """
    Fetches the state options from the API and returns them as a list of options.
    """
    response = requests.get(f"{Config.BASE_URL}/state?api_key={Config.API_KEY}")
    response.raise_for_status()
    data = response.json()['data']
    return [(state['id'], state['name']) for state in data]

def test_state_endpoint(state_id=None):
    """
    Tests the /arms/state API endpoint with an optional state_id parameter.
    """
    print("\nTesting /arms/state Endpoint")
    try:
        url = f"{Config.BASE_URL}/state"
        params = {"api_key": Config.API_KEY}
        if state_id is not None:
            params['id'] = state_id
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/state_data.csv")
        browser_url = generate_browser_url(url, params)
        print(f"Browser URL: {browser_url}")

        # Print the response data
        print(data)
        
    except requests.RequestException as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    state_options = get_state_options()
    print("Available States:")
    for id, name in state_options:
        print(f"{id}: {name}")
    
    selected_id = input("Enter State ID to test, or leave empty to fetch all: ").strip()
    if selected_id:
        test_state_endpoint(selected_id)
    else:
        test_state_endpoint()

```
## modules/year.py
```
# year.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def get_year_options():
    """
    Fetches the available years from the API and returns them as a list of options.
    """
    response = requests.get(f"{Config.BASE_URL}/year?api_key={Config.API_KEY}")
    response.raise_for_status()
    data = response.json()['data']
    return data  # Assuming the API returns a list of years

def test_year_endpoint(year=None):
    """
    Tests the /arms/year API endpoint with an optional year parameter.
    """
    print("\nTesting /arms/year Endpoint")
    try:
        url = f"{Config.BASE_URL}/year"
        params = {"api_key": Config.API_KEY}
        if year is not None:
            params['year'] = year
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/year_data.csv")
        browser_url = generate_browser_url(url, params)
        print(f"Browser URL: {browser_url}")

        print(data)
    except requests.RequestException as e:
        print(f"Error: {e}")

    
# Example usage
if __name__ == "__main__":
    year_options = get_year_options()
    print("Available Years:")
    for year in year_options:
        print(year)
    
    selected_year = input("Enter Year to test, or leave empty to fetch all: ").strip()
    if selected_year:
        test_year_endpoint(selected_year)
    else:
        test_year_endpoint()

```
## modules/report.py
```
# report.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_report_endpoint():
    print("\nTesting /arms/report Endpoint")
    try:
        response = requests.get(f"{Config.BASE_URL}/report?api_key={Config.API_KEY}")
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/report_data.csv")
        browser_url = generate_browser_url(Config.BASE_URL, "/report", Config.API_KEY)
        print(f"Browser URL: {browser_url}")

        # Adjusted to handle JSON response
        if isinstance(data, dict):
            print(data)
        elif isinstance(data, list):
            print(data[:5])
    except requests.RequestException as e:
        print(f"Error: {e}")

```
## modules/variable.py
```
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

```
## modules/surveydata.py
```
# surveydata.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_surveydata_endpoint(year=None, variable=None):
    print("\nTesting /arms/surveydata Endpoint")
    try:
        url = f"{Config.BASE_URL}/surveydata"
        params = {"api_key": Config.API_KEY}
        post_data = {}
        if year:
            post_data['year'] = [year]
        if variable:
            post_data['variable'] = variable

        response = requests.post(url, params=params, json=post_data)
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/surveydata.csv")
        browser_url = generate_browser_url(url, params)
        print(f"Browser URL: {browser_url}")

        print(data)
    except requests.RequestException as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    selected_year = input("Enter Year (optional): ").strip()
    selected_variable = input("Enter Variable (optional): ").strip()
    test_surveydata_endpoint(selected_year, selected_variable)

```
## modules/farmtype.py
```
# farmtype.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def get_farmtype_options():
    """
    Fetches the farm types from the API and returns them as a list of options.
    """
    response = requests.get(f"{Config.BASE_URL}/farmtype?api_key={Config.API_KEY}")
    response.raise_for_status()
    data = response.json()['data']
    return [(ft['id'], ft['name']) for ft in data]

def test_farmtype_endpoint(farmtype_id=None):
    """
    Tests the /arms/farmtype API endpoint with an optional farmtype_id parameter.
    """
    print("\nTesting /arms/farmtype Endpoint")
    try:
        url = f"{Config.BASE_URL}/farmtype"
        params = {"api_key": Config.API_KEY}
        if farmtype_id is not None:
            params['id'] = farmtype_id
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/farmtype_data.csv")
        browser_url = generate_browser_url(url, params)
        print(f"Browser URL: {browser_url}")

        # Print the response data
        print(data)
        
    except requests.RequestException as e:
        print(f"Error: {e}")

    
# Example usage
if __name__ == "__main__":
    farmtype_options = get_farmtype_options()
    print("Available Farm Types:")
    for id, name in farmtype_options:
        print(f"{id}: {name}")
    
    selected_id = input("Enter Farm Type ID to test, or leave empty to fetch all: ").strip()
    if selected_id:
        test_farmtype_endpoint(selected_id)
    else:
        test_farmtype_endpoint()

```
## modules/category.py
```
# category.py
import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def get_category_options():
    response = requests.get(f"{Config.BASE_URL}/category?api_key={Config.API_KEY}")
    response.raise_for_status()
    data = response.json()['data']
    return [(category['id'], category['name']) for category in data]

def test_category_endpoint(category_id=None):
    print("\nTesting /arms/category Endpoint")
    try:
        url = f"{Config.BASE_URL}/category"
        params = {"api_key": Config.API_KEY}
        if category_id is not None:
            params['id'] = category_id

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        csv_file_path = write_to_csv(data, "data/storage/category_data.csv")
        browser_url = generate_browser_url(url, params)
        print(f"Browser URL: {browser_url}")

        print(data)
    except requests.RequestException as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    category_options = get_category_options()
    print("Available Categories:")
    for id, name in category_options:
        print(f"{id}: {name}")

    selected_id = input("Enter Category ID to test, or leave empty to fetch all: ").strip()
    if selected_id:
        test_category_endpoint(selected_id)
    else:
        test_category_endpoint()

```
