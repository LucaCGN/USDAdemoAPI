import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

# New function for fetching subcategory details
def fetch_subcategories(category_name):
    url = f"{Config.BASE_URL}/category"
    data = {"name": category_name}
    response = requests.post(url, json=data, params={"api_key": Config.API_KEY})
    response.raise_for_status()
    return response.json()

# Function to get a list of categories
def get_category_options():
    response = requests.get(f"{Config.BASE_URL}/category?api_key={Config.API_KEY}")
    response.raise_for_status()
    data = response.json()['data']
    return [(category['id'], category['name']) for category in data]

# Function to get detailed info for a specific category
def get_detailed_category_info(category_name):
    url = f"{Config.BASE_URL}/category"
    data = {"name": category_name}
    response = requests.post(url, json=data, params={"api_key": Config.API_KEY})
    response.raise_for_status()
    return response.json()

# Function to test the category endpoint
def test_category_endpoint(category_id=None):
    print("\nTesting /arms/category Endpoint")
    try:
        url = f"{Config.BASE_URL}/category"
        if category_id:
            options = get_category_options()
            full_name = next((name for id, name in options if id == category_id), None)
            if not full_name:
                print(f"No category found with ID '{category_id}'.")
                return

            data = get_detailed_category_info(full_name)
            params = {"api_key": Config.API_KEY, "name": full_name}

            csv_file_path = write_to_csv(data, "data/storage/category_data.csv")
            browser_url = generate_browser_url(url, params)
            print(f"Browser URL: {browser_url}")
            print(f"Data saved to CSV file: {csv_file_path}")

            print(data)

            # Prompt to fetch subcategories
            if input("Do you want to view subcategories? (y/n): ").lower() == 'y':
                subcategory_data = fetch_subcategories(full_name)
                print("Subcategories:")
                print(subcategory_data)
        else:
            options = get_category_options()
            print("Available Categories:")
            for id, name in options:
                print(f"{id}: {name}")
            
    except requests.RequestException as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    print("Enter Category ID to get detailed information, or leave empty to list all categories:")
    selected_id = input().strip()
    test_category_endpoint(selected_id)
