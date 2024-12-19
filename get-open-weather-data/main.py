from owm_key import owm_api_key
import requests
from tabulate import tabulate


def get_weather_data(place, api_key=None):
    if api_key is None or len(place) < 2:
        return None

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')

    res_obj = res.json()
    print(res_obj)
    head = ["City", "Country", "Lat", "Lon", "UTC", "Feels Like"]

    utc_offset = res_obj['timezone'] // 3600
    if utc_offset > 0:
        utc_str = f"UTC+{utc_offset}"
    else:
        utc_str = f"UTC{utc_offset}"

    temp = res_obj['main']['feels_like'] - 273.15

    mydata = [
         [res_obj['name'],
          res_obj['sys']['country'],
          res_obj['coord']['lat'],
          res_obj['coord']['lon'],
          utc_str,
          temp]
    ]

    print(tabulate(mydata, headers=head, tablefmt="grid"))

    return mydata


if __name__ == '__main__':
    get_weather_data('Chicago', api_key=owm_api_key)
    get_weather_data('Saint Petersburg', api_key=owm_api_key)
    get_weather_data('Dhaka', api_key=owm_api_key)
