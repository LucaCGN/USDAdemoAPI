# state.py
# Module for testing the /arms/state endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_state_endpoint():
    """
    Tests the /arms/state API endpoint and handles the response.
    """
    print("\nTesting /arms/state Endpoint")

    try:
        # Making a GET request to the /arms/state endpoint
        response = requests.get(f"{Config.BASE_URL}/state?api_key={Config.API_KEY}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "state_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/state", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/state: {e}")