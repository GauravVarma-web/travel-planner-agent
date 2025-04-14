# actions.py
def get_destination_weather(city):
    """Get weather forecast for a destination city"""
    # Hardcoded data for demonstration
    weather_data = {
        "New York": {"temp": "72°F", "conditions": "Partly cloudy"},
        "Paris": {"temp": "65°F", "conditions": "Sunny"},
        "Tokyo": {"temp": "78°F", "conditions": "Rainy"},
        "London": {"temp": "60°F", "conditions": "Foggy"},
        "Sydney": {"temp": "80°F", "conditions": "Clear"}
    }
    
    if city in weather_data:
        return weather_data[city]
    else:
        return {"temp": "Unknown", "conditions": "Unknown"}

def get_flight_info(origin, destination):
    """Get flight information between two cities"""
    # Hardcoded data for demonstration
    flight_data = {
        ("New York", "London"): {"duration": "7h 30m", "price": "$750"},
        ("New York", "Paris"): {"duration": "7h 45m", "price": "$800"},
        ("London", "Paris"): {"duration": "1h 15m", "price": "$200"},
        ("Tokyo", "Sydney"): {"duration": "9h 45m", "price": "$900"},
        ("London", "Tokyo"): {"duration": "11h 45m", "price": "$1100"}
    }
    
    key = (origin, destination)
    if key in flight_data:
        return flight_data[key]
    # Check for reverse route
    key = (destination, origin)
    if key in flight_data:
        return flight_data[key]
    
    return {"duration": "Unknown", "price": "Unknown"}

def recommend_attractions(city):
    """Recommend tourist attractions in a city"""
    # Hardcoded data for demonstration
    attractions = {
        "New York": ["Empire State Building", "Central Park", "Times Square"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "Notre Dame Cathedral"],
        "Tokyo": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing"],
        "London": ["Big Ben", "British Museum", "London Eye"],
        "Sydney": ["Sydney Opera House", "Bondi Beach", "Harbour Bridge"]
    }
    
    if city in attractions:
        return attractions[city]
    else:
        return ["No attractions found"]