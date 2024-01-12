# utils/url_generator.py
def generate_browser_url(base_url, params):
    """
    Generates a browser-accessible URL for the given endpoint and parameters.
    """
    query_string = "&".join([f"{key}={value}" for key, value in params.items()])
    return f"{base_url}?{query_string}"
