from main import get_weather_data
import pytest

key = 'b4aeb20242213e0f0bd25f9d5d7063f5'


def test_without_key():
    assert get_weather_data(
        "Moscow") is None, \
        " Для получения данных необходимо задать значение для api_key "


def test_in_riga():
    assert get_weather_data("Riga",
                            api_key=key) is not None, \
        " Type of response is not none while using the key "


def test_type_of_res():
    assert type(get_weather_data("Riga",
                                 api_key=key)) is list, \
        " Type of response is not none while using the key "


def test_args_error():
    assert get_weather_data('') is None, \
        " There should be one positional argument: 'city' and one keyword argument 'key_arg'"


def test_pos_arg_error():
    assert get_weather_data('',
                            api_key=key) is None, \
        " There should be one positional argument: 'city' "


def test_temp_type():
    import json

    assert type(get_weather_data('Riga', api_key=key)[0][5]) is float, \
        " Error with type of feels_like attribute "


inp_params_1 = "city, api_key, expected_country"
exp_params_countries = [("Chicago", key, 'US'),
                        ("Saint Petersburg", key, 'RU'), ("Dakka", key, 'BD'),
                        ("Minsk", key, 'BY'), ("Kioto", key, 'JP'),
                        ("Anchorage", key, 'US'), ("Havana", key, 'CU')]


@pytest.mark.parametrize(inp_params_1, exp_params_countries)
def test_countries(city, api_key, expected_country):

    assert get_weather_data(city, api_key=key)[0][1] == expected_country, \
        " Error with country code "


inp_params_2 = "city, api_key, expected_time"
exp_params_timezones = ([("Chicago", key, 'UTC-6'),
                        ("Saint Petersburg", key, 'UTC+3'),
                        ("Dakka", key, 'UTC+6'), ("Minsk", key, 'UTC+3'),
                        ("Kioto", key, 'UTC+9'), ("Anchorage", key, 'UTC-9'),
                        ("Havana", key, 'UTC-5')])


@pytest.mark.parametrize(inp_params_2, exp_params_timezones)
def test_utc_time(city, api_key, expected_time):
    assert get_weather_data(city, api_key=key)[0][4] == expected_time, \
        " Error with timezone "
