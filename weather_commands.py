import re
import requests


def weather_command_answer(user_msg):
    city = extract_weather_city_name(user_msg)
    # Capitalize the first letter of each word in the city name
    city = ' '.join(word.capitalize() for word in city.split())
    answer = weather_answer(city)
    print(answer)
    return answer


def extract_weather_city_name(sentence):
    try:
        # Update the pattern to capture everything after 'weather in ' including spaces
        pattern = r'weather in (.+)'

        match = re.search(pattern, sentence, re.IGNORECASE)
        if match:
            return match.group(1).strip()  # Remove any extra leading/trailing spaces

        return None
    except Exception as e:
        return f"Error: {e}"


def weather_answer(city):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        'latitude': None,
        'longitude': None,
        'current_weather': True,
        'timezone': 'auto'
    }

    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geocoding_response = requests.get(geocoding_url)

    if geocoding_response.status_code != 200:
        return "Could not retrieve location data."

    location_data = geocoding_response.json()
    if not location_data['results']:
        return "City not found."

    # Set the latitude and longitude for the weather request
    params['latitude'] = location_data['results'][0]['latitude']
    params['longitude'] = location_data['results'][0]['longitude']

    weather_response = requests.get(url, params=params)

    if weather_response.status_code != 200:
        return "Could not retrieve weather data."

    weather_data = weather_response.json()
    if not weather_data.get('current_weather'):  # Ensure it exists before accessing it
        return "Could not retrieve weather data."

    current_weather = weather_data['current_weather']

    # Ensure the temperature is valid before using it
    if 'temperature' not in current_weather:
        return "Weather data is incomplete."

    weather = f"Location: {city} Temperature: {current_weather['temperature']}"

    return weather