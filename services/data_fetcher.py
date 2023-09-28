import requests

def get_average_price():
    url = "http://localhost:8080/get-properties"
    
    response = requests.get(url)
    properties = response.json()
 
    total_price = sum([property["price"] for property in properties])
    average_price = total_price / len(properties)

    return average_price

