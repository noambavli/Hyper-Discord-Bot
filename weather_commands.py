import re
import requests


def weather_command_answer(user_msg):
    try:
        city = extract_weather_city_name(user_msg)
        if not city:
            return "Please specify a city."

        # Capitalize the first letter of each word in the city name
        city = ' '.join(word.capitalize() for word in city.split())
        answer = weather_answer(city)

        if "Error" in answer:
            return f"An error occurred: {answer}"

        return answer
    except Exception as e:
        return f"Error in processing your request: {e}"


def extract_weather_city_name(sentence):
    try:
        # Update the pattern to capture everything after 'weather in ' including spaces
        pattern = r'weather in (.+)'

        match = re.search(pattern, sentence, re.IGNORECASE)
        if match:
            return match.group(1).strip()

        return None
    except Exception as e:
        return f"Error while extracting city name: {e}"


def weather_answer(city):
    try:
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
            return f"Error: Could not retrieve location data. Status code: {geocoding_response.status_code}"

        location_data = geocoding_response.json()
        if not location_data.get('results'):
            return "City not found."

        params['latitude'] = location_data['results'][0]['latitude']
        params['longitude'] = location_data['results'][0]['longitude']

        # Handle weather API request
        weather_response = requests.get(url, params=params)

        if weather_response.status_code != 200:
            return f"Error: Could not retrieve weather data. Status code: {weather_response.status_code}"

        weather_data = weather_response.json()

        if not weather_data.get('current_weather'):
            return "Error: Weather data is incomplete."

        current_weather = weather_data['current_weather']

        if 'temperature' not in current_weather:
            return "Error: Weather data is incomplete."

        weather = f"Location: {city} Temperature: {current_weather['temperature']}°C"

        return weather
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Error: {e}"
