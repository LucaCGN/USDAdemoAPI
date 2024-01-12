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
