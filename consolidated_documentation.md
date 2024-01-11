## modules/surveydata.py
```
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

```
## modules/state.py
```
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
```
## main.py
```
# main.py
# Main file for the ARMS Data API Tester & Explorer application

import sys
from modules import state, year, surveydata, category, report, variable, farmtype

def main_menu():
    """
    Displays the main menu of the application.
    """
    print("\nARMS Data API Tester & Explorer")
    print("--------------------------------")
    print("1: Test /arms/state Endpoint")
    print("2: Test /arms/year Endpoint")
    print("3: Test /arms/surveydata Endpoint")
    print("4: Test /arms/category Endpoint")
    print("5: Test /arms/report Endpoint")
    print("6: Test /arms/variable Endpoint")
    print("7: Test /arms/farmtype Endpoint")
    print("0: Exit")
    print("--------------------------------")
    
    choice = input("Enter your choice: ")
    return choice

def execute_choice(choice):
    """
    Executes the selected choice from the main menu.
    """
    if choice == "1":
        state.test_state_endpoint()
    elif choice == "2":
        year.test_year_endpoint()
    elif choice == "3":
        surveydata.test_surveydata_endpoint()
    elif choice == "4":
        category.test_category_endpoint()
    elif choice == "5":
        report.test_report_endpoint()
    elif choice == "6":
        variable.test_variable_endpoint()
    elif choice == "7":
        farmtype.test_farmtype_endpoint()
    elif choice == "0":
        sys.exit("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        choice = main_menu()
        execute_choice(choice)

if __name__ == "__main__":
    main()
```
## modules/variable.py
```
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

```
## utils/url_generator.py
```
# url_generator.py
# Utility script for generating browser URLs in the ARMS Data API Tester & Explorer application

def generate_browser_url(base_url, endpoint, api_key):
    """
    Generates a browser-accessible URL for the given endpoint and API key.
    """
    return f"{base_url}{endpoint}?api_key={api_key}"

```
## modules/report.py
```
# report.py
# Module for testing the /arms/report endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_report_endpoint():
    """
    Tests the /arms/report API endpoint and handles the response.
    """
    print("\nTesting /arms/report Endpoint")

    try:
        # Making a GET request to the /arms/report endpoint
        response = requests.get(f"{Config.BASE_URL}/report?api_key={Config.API_KEY}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "report_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/report", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/report: {e}")

```
## README.md
```

```
## requirements.txt
```
requests==2.25.1
pandas==1.2.4

```
## modules/year.py
```
# year.py
# Module for testing the /arms/year endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_year_endpoint():
    """
    Tests the /arms/year API endpoint and handles the response.
    """
    print("\nTesting /arms/year Endpoint")

    try:
        # Making a GET request to the /arms/year endpoint
        response = requests.get(f"{Config.BASE_URL}/year?api_key={Config.API_KEY}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "year_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/year", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/year: {e}")

```
## config.py
```
# config.py
# Configuration file for ARMS Data API Tester & Explorer application

class Config:
    BASE_URL = "https://api.ers.usda.gov/data/arms"  # Base URL for the ARMS Data API
    API_KEY = "YOUR_API_KEY"  # Placeholder for the API key
```
## modules/category.py
```
# category.py
# Module for testing the /arms/category endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_category_endpoint():
    """
    Tests the /arms/category API endpoint and handles the response.
    """
    print("\nTesting /arms/category Endpoint")

    try:
        # Making a GET request to the /arms/category endpoint
        response = requests.get(f"{Config.BASE_URL}/category?api_key={Config.API_KEY}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "category_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/category", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/category: {e}")

```
## utils/api_request_handler.py
```
# api_request_handler.py
# Utility script for handling API requests in the ARMS Data API Tester & Explorer application

import requests

def make_api_request(url, method='GET', data=None):
    """
    Makes an API request to the given URL with the specified method and data.
    """
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        else:
            raise ValueError("Unsupported HTTP method specified.")

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"API Request Error: {e}")
        return None

```
## modules/farmtype.py
```
# farmtype.py
# Module for testing the /arms/farmtype endpoint in the ARMS Data API Tester & Explorer application

import requests
from config import Config
from utils.csv_writer import write_to_csv
from utils.url_generator import generate_browser_url

def test_farmtype_endpoint():
    """
    Tests the /arms/farmtype API endpoint and handles the response.
    """
    print("\nTesting /arms/farmtype Endpoint")

    try:
        # Making a GET request to the /arms/farmtype endpoint
        response = requests.get(f"{Config.BASE_URL}/farmtype?api_key={Config.API_KEY}")
        response.raise_for_status()

        # Processing the response
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully. Writing to CSV and displaying URL.")

            # Writing data to CSV
            csv_file_path = write_to_csv(data, "farmtype_data.csv")

            # Displaying the URL for browser access
            browser_url = generate_browser_url(Config.BASE_URL, "/farmtype", Config.API_KEY)
            print(f"Browser URL: {browser_url}")

            # Display a preview of the results
            print("Preview of the results:")
            print(data[:5])  # Displaying the first 5 records as a preview

    except requests.RequestException as e:
        print(f"Error fetching data from /arms/farmtype: {e}")

```
## utils/csv_writer.py
```
# csv_writer.py
# Utility script for writing data to CSV in the ARMS Data API Tester & Explorer application

import csv

def write_to_csv(data, filename):
    """
    Writes the given data to a CSV file with the specified filename.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if isinstance(data, list) and len(data) > 0:
            # Writing headers
            writer.writerow(data[0].keys())
            # Writing data rows
            for row in data:
                writer.writerow(row.values())
        return filename

```
