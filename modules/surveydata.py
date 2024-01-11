# surveydata.py
# Module for testing the /arms/surveydata endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_surveydata_endpoint():
    """
    Tests the /arms/surveydata API endpoint and handles the response.
    """
    print("\nTesting /arms/surveydata Endpoint")

    try:
        # Example POST request data
        post_data = {
            "year": [2023],
            "variable": "igovtt"
        }

        # Making a POST request to the /arms/surveydata endpoint
        response = requests.post(f"{Config.BASE_URL}/surveydata?api_key={Config.API_KEY}", json=post_data)
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "surveydata.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/surveydata", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/surveydata: {e}")
