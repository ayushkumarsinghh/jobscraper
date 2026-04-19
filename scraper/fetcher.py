import requests
from config import URL, HEADERS

def fetch_page():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the API: {e}")
        return []