import services

def average_price(properties):
    # Calculates average property prices.
    total_price = sum(prop['price'] for prop in properties)
    return total_price / len(properties)

def average_price_by_location(properties, location_key='address'):
    # Calculate average prices by location.
    location_prices = {}
    
    for prop in properties:
        location = prop[location_key]
        if location not in location_prices:
            location_prices[location] = []
        location_prices[location].append(prop['price'])
    
    location_avg_prices = {}
    for location, prices in location_prices.items():
        location_avg_prices[location] = sum(prices) / len(prices)
        
    return location_avg_prices

def properties_below_average(properties):
    # Identifies properties priced below the general average.
    avg_price = average_price(properties)
    return [prop for prop in properties if prop['price'] < avg_price]

