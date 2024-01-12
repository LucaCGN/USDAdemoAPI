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
