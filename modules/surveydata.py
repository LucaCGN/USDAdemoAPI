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
