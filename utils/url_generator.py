# url_generator.py
# Utility script for generating browser URLs in the ARMS Data API Tester & Explorer application

def generate_browser_url(base_url, endpoint, api_key):
    """
    Generates a browser-accessible URL for the given endpoint and API key.
    """
    return f"{base_url}{endpoint}?api_key={api_key}"
