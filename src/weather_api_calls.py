import requests
from src.weather_details import WeatherDetails
from typing import Dict, Optional


def retrieve_current_weather(city: str, state_code: str) -> Optional[Dict]:
    """
    Retrieves the current data of a city
    :param city: The name of the city
    :param state_code: The state code that the city is in

    :return: A dict that represents the json file read from the api call
    or None if the API call failed to read a city
    """
    city_cleaned = city.strip()
    state_code_cleaned = state_code.strip()
    if city_cleaned == "" or state_code_cleaned == "":
        return None
    api_key = "76ddb44c85f8d322138c2ca556f7245f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_cleaned},{state_code_cleaned},us&appid={api_key}"
    response = requests.get(url)
    weather_json: Dict = response.json()
    if weather_json.get("message") == "city not found":
        return None
    return response.json()


def create_weather(weather_json: Dict) -> WeatherDetails:
    """
    Creates a WeatherDetails using a dictionary that represents the json read
    from the openWeatherAPI
    :param weather_json: The json file read
    :return: The WeatherDetails that was created with the parsed json
    """
    # Collect atmosphere data such as temp and humidity
    main_data: Dict = weather_json.get("main")
    temp_in_k: float = main_data.get("temp")
    temp_feels_like_in_k: float = main_data.get("feels_like")
    temp_min_in: float = main_data.get("temp_min")
    temp_max_in: float = main_data.get("temp_max")
    humidity: int = main_data.get("humidity")
    # Collect wind speed
    wind_data: Dict = weather_json.get("wind")
    wind_speed: float = wind_data.get("speed")
    # City name
    city_name = weather_json.get("name")
    return WeatherDetails(
        temp_in_k,
        temp_feels_like_in_k,
        temp_max_in,
        temp_min_in,
        humidity,
        wind_speed,
        city_name,
    )
