from src.weather_details import WeatherDetails


def convert_kelvin_to_celsius(temp_in_k: float) -> int:
    """
    Converts kelvin to Celsius
    :param temp_in_k: The temperature in Celsius
    :return: The rounded temperature in Celsius
    """
    # Round since we only care about the nearest degree and helps avoid
    # floating point math later
    return round(temp_in_k - 273.15)


class MetricWeatherDetails(WeatherDetails):
    """
    Child object that represents weather data with Metric measurements
    """
    def __init__(self, weather_details: WeatherDetails):
        WeatherDetails.__init__(
            self,
            # The typical temperature data read from the API call is in kelvin,
            # so it needs to be converted to Celsius to be in Metric.
            convert_kelvin_to_celsius(weather_details.temp),
            convert_kelvin_to_celsius(weather_details.temp_feels_like),
            convert_kelvin_to_celsius(weather_details.temp_max),
            convert_kelvin_to_celsius(weather_details.temp_min),
            weather_details.humidity,
            # Round the wind to avoid floating point math.
            round(weather_details.wind_speed),
            weather_details.city_name,
            temp_unit="\N{DEGREE SIGN}" + "C",
            wind_unit="m/s",
        )
