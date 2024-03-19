import pytest

from src.weather_api_calls import retrieve_current_weather


@pytest.mark.parametrize(
    "city, state_code", [("New York", "NY"), # Try location with space
                         ("Bismarck", "ND"), # Try location with no spaces
                         (" New York ", " NY ")] # Try location with trailing whitespace
)
def test_retrieve_current_weather_call(city: str, state_code: str):
    """
    Tests what should be considered valid input
    :param city: The valid city
    :param state_code: The valid state code
    :return:
    """
    assert isinstance(retrieve_current_weather(city, state_code), dict)


@pytest.mark.parametrize("city, state_code", [("NA", "NA"),
                                              ("", "")])
def test_retrieve_current_weather_call_fail(city, state_code):
    """
    Tests input that should return None
    :param city: The invalid city
    :param state_code: The invalid state code
    :return:
    """
    assert retrieve_current_weather("", "") is None
