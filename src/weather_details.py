class WeatherDetails:
    """
    Object that represents the default data read from the openWeatherAPI
    """
    def __init__(
        self,
        temp_in_k: float,
        temp_feels_like_in_k: float,
        temp_max_in_k: float,
        temp_min_in_k: float,
        humidity: int,
        wind_speed: float,
        city_name: str,
        temp_unit: str = "\N{DEGREE SIGN}" + "K",
        wind_unit: str = "m/s",
    ):
        """
        Creates the WeatherDetails object using the read data
        :param temp_in_k: Current temperature in kelvin
        :param temp_feels_like_in_k: Current real feel temp in kelvin
        :param temp_max_in_k: Daily Max in kelvin
        :param temp_min_in_k: Daily Min in kelvin
        :param humidity: Current humidity
        :param wind_speed: Current wind speed in meters per second
        :param city_name: The name of the city
        """
        # Convert all the units into imperial units
        self.temp: float = temp_in_k
        self.temp_feels_like: float = temp_feels_like_in_k
        self.temp_min: float = temp_min_in_k
        self.temp_max: float = temp_max_in_k
        self.humidity: int = humidity
        # Collect wind data
        self.wind_speed: float = wind_speed
        # City name
        self.city_name = city_name

        self.temp_unit = temp_unit
        self.wind_unit = wind_unit

    def compare(self, other):
        """
        Compares the weather details of this weather details with and returns a
        WeatherDetail that returns the absolute value difference between the two
        :param other: The other weather details that is being compared
        :return: The new weatherDifference with the difference in weather
        """

        temp_difference: float | int = abs(self.temp - other.temp)
        temp_feel_difference: float | int = abs(self.temp_feels_like - other.temp_feels_like)
        temp_max_difference: float | int = abs(self.temp_max - other.temp_max)
        temp_min_difference: float | int = abs(self.temp_min - other.temp_min)
        humidity_difference: int = abs(self.humidity - other.humidity)
        wind_speed: float | int = abs(self.wind_speed - other.wind_speed)
        city_name: str = f"Difference between {self.city_name} and {other.city_name}"
        return WeatherDetails(
            temp_difference,
            temp_feel_difference,
            temp_max_difference,
            temp_min_difference,
            humidity_difference,
            wind_speed,
            city_name,
            self.temp_unit,
            self.wind_unit,
        )
