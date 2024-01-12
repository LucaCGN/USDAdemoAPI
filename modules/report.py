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
