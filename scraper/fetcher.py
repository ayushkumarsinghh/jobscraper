import requests
from config import URL, HEADERS

def fetch_page():
    response = requests.get(URL, headers=HEADERS)
    return response.text