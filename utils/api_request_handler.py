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
