from prettytable import PrettyTable
from src.weather_api_calls import retrieve_current_weather, create_weather
from src.weather_details import WeatherDetails
from src.imperial_weather_details import ImperialWeatherDetails
from src.metric_weather_details import MetricWeatherDetails


def create_row_in_table(table: PrettyTable, weather_details: WeatherDetails):
    """
    Adds a columns of weather details to a provided table
    :param table: The PrettyTable that is having its columns updated
    :param weather_details: The WeatherDetails that is being added to the table
    """
    table.add_column(
        weather_details.city_name,
        [
            f"{weather_details.temp} {weather_details.temp_unit}",
            f"{weather_details.temp_feels_like} {weather_details.temp_unit}",
            f"{weather_details.temp_max} {weather_details.temp_unit}",
            f"{weather_details.temp_min} {weather_details.temp_unit}",
            f"{weather_details.humidity}%",
            f"{weather_details.wind_speed} {weather_details.wind_unit}",
        ],
    )


def display_comparison_table(
    is_imperial: bool, city_1: WeatherDetails, city_2: WeatherDetails
):
    """
    Displays a formatted table that displays the weather attributes of two
    cities along with the differences of the two cities
    :param is_imperial: Indicates whether the data is displayed in Imperial
    or Metric
    :param city_1: The WeatherDetails of the first city
    :param city_2: The WeatherDetails of the second city
    """

    # Pretty table is used to create a nice and readable table to display
    # Weather table
    comparison_table: PrettyTable = PrettyTable()
    # Set up the labels of each row
    comparison_table.add_column(
        "Weather Traits",
        [
            "Temperature",
            "Real Feel",
            "Daily Max",
            "Daily Min",
            "Humidity",
            "Wind Speed",
        ],
    )
    # Convert the temperature into a more common measurement systems
    if is_imperial:
        city_1_converted = ImperialWeatherDetails(city_1)
        city_2_converted = ImperialWeatherDetails(city_2)
    else:
        city_1_converted = MetricWeatherDetails(city_1)
        city_2_converted = MetricWeatherDetails(city_2)

    # Create the rest of the table using the weather
    create_row_in_table(comparison_table, city_1_converted)
    create_row_in_table(comparison_table, city_2_converted)
    create_row_in_table(comparison_table, city_1_converted.compare(city_2_converted))

    print(comparison_table)


def prompt_for_weather() -> dict | None:
    """
    Prompts the user for a city and its state code
    :return: WeatherDetails if the city was found and None if it was not
    """
    weather: dict | None = None
    while weather is None:
        city: str | None = None
        while city is None:
            city = input("Please input the city's name ")
        # Ask for the state code since multiple cities have the same name
        state_code: str | None = None
        while state_code is None:
            state_code = input("Please input the state code ")
        weather = retrieve_current_weather(city, state_code)
    return weather


def print_menu_and_get_input():
    """
    Prints the main menu and prompts the user if they would like to keep using
    the application
    :return: True if the user wants to use the app and False if they are done
    """
    input_given: str = input(
        """Type 1 to compare two cities
Type 2 to exit the program
"""
    ).strip(" ")

    while input_given != "1" and input_given != "2":
        input_given = input(
            f"""The input {input_given} is not valid!
Type 1 to compare two cities
Type 2 to exit the program
"""
        ).strip(" ")
    # Indicate that the user wants to run the application
    if input_given == "1":
        return True
    # Indicate that the user is done with the application
    else:
        return False


def print_menu_and_get_measurement_system() -> bool:
    """
    Prints a menu and prompts the user for which measurement system they would
    like to read
    :return: True if Imperial or False if Metric
    """
    input_given: str = input(
        """Type 1 to retrieve data in Imperial
Type 2 to retrieve data in Metric
"""
    ).strip(" ")

    while input_given != "1" and input_given != "2":
        input_given: str = input(
            """Type 1 to retrieve data in Imperial
Type 2 to retrieve data in Metric
"""
        ).strip(" ")
    # Indicate that the user wants the data in Imperial
    if input_given == "1":
        return True
    # Indicate that the user wants the data in Metric
    else:
        return False


def prompt_and_retrieve_weather_data() -> dict:
    """
    Asks for a location and obtains the weather data

    :return: The dictionary represented with a dictionary
    """
    weather_data_from_location: dict | None = prompt_for_weather()
    while weather_data_from_location is None:
        print("Data could not be retrieve please double check the inputs")
        weather_data_from_location = prompt_for_weather()
    return weather_data_from_location


def main():
    print("Welcome to the weather compare command line utility")
    start_input: bool = print_menu_and_get_input()
    while start_input:
        # First we grab two locations given by the user
        weather_data_from_location_1 = prompt_and_retrieve_weather_data()
        weather_data_from_location_2 = prompt_and_retrieve_weather_data()
        # Both locations have given us data lets create WeatherDetails to get more readable data
        weather_details_from_location_1: WeatherDetails = create_weather(
            weather_data_from_location_1
        )
        weather_details_from_location_2: WeatherDetails = create_weather(
            weather_data_from_location_2
        )
        # Print out a table comparing the two
        display_comparison_table(
            print_menu_and_get_measurement_system(),
            weather_details_from_location_1,
            weather_details_from_location_2,
        )
        # Prompt the user again to see if the program continues
        start_input = print_menu_and_get_input()
    print("Thank you for using our application. Have a nice day.")


if __name__ == "__main__":
    main()
