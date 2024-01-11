# variable.py
# Module for testing the /arms/variable endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_variable_endpoint(variable_id):
    """
    Tests the /arms/variable API endpoint and handles the response.
    """
    print(f"\nTesting /arms/variable Endpoint for Variable ID: {variable_id}")

    try:
        # Making a GET request to the /arms/variable endpoint with a specific variable ID
        response = requests.get(f"{Config.BASE_URL}/variable?api_key={Config.API_KEY}&id={variable_id}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, f"variable_{variable_id}_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, f"/variable?id={variable_id}", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data)

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/variable: {e}")
