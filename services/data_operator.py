import requests
import logging
import utils

BASE_URL = "http://localhost:8080"

def collect_data(endpoint="/get-properties"):
    url = BASE_URL + endpoint
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        properties = response.json()
        return properties

    except requests.RequestException as e:
        logging.error(f"Error accessing URL: {e}")
        return None

def spread_data(payload, endpoint="/add-insights"):
    url = BASE_URL + endpoint

    try:
        response = requests.post(url, json=payload, headers=utils.headers.get_basic_headers())

        if response.status_code == 200:
            logging.info(response.text)
            logging.info(f"Add in Insight table {payload}")
            return response
        else:
            logging.error(f"Request error: Code {response.text}")
            return response

    except requests.RequestException as e:
        logging.error(f"Error accessing URL: {e}")
        return response
        
