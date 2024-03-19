from src.weather_details import WeatherDetails


def convert_kelvin_to_fahrenheit(temp_in_k: float) -> int:
    """
    Converts kelvin to Fahrenheit
    :param temp_in_k: The temperature in kelvin
    :return: The rounded temperature in Fahrenheit
    """
    # Round since we only care about the nearest degree and helps avoid
    # floating point math later when comparing
    return round((temp_in_k - 273.15) * 9 / 5 + 32)


def convert_meters_per_sec_to_miles_per_hour(meters_per_seconds: float) -> int:
    """
    Converts meters per second to miles per hour
    :param meters_per_seconds: The number in meters per seconds
    :return: The converted number in miles per hour
    """
    # Round to avoid floating point math
    return round(meters_per_seconds * 2.237)


class ImperialWeatherDetails(WeatherDetails):
    """
    Child object that represents weather data with Imperial measurements
    """
    def __init__(self, weather_details: WeatherDetails):
        """
        Creates an Imperial measurement system WeatherDetails
        :param weather_details: The weather details read from the spec
        """
        WeatherDetails.__init__(
            self,
            # The temperature data read from the API call is in kelvin, so
            # it needs to be converted to Fahrenheit to be in Imperial.
            convert_kelvin_to_fahrenheit(weather_details.temp),
            convert_kelvin_to_fahrenheit(weather_details.temp_feels_like),
            convert_kelvin_to_fahrenheit(weather_details.temp_max),
            convert_kelvin_to_fahrenheit(weather_details.temp_min),
            weather_details.humidity,
            # The wind speed data read from the API call is in meters per
            # second, so it needs to be converted to miles per hour to be in
            # Imperial.
            convert_meters_per_sec_to_miles_per_hour(weather_details.wind_speed),
            weather_details.city_name,
            temp_unit="\N{DEGREE SIGN}" + "F",
            wind_unit="MPH",
        )
