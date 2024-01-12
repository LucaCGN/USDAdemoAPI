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
