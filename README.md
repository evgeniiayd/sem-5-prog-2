<<<<<<< HEAD
# openweatherapi

## Описание задачи
Написать реализацию функции  ```get_weather_data(place, api_key=None)``` (в модуле ```getweatherdata```), в которой необходимо получить данные о погоде с сайта https://openweathermap.org/. 

Функция должна возвращать объект в формате JSON, включающий: 
- информацию о названии города (в контексте openweathermap),
- код страны (2 символа),
- широту и долготу, на которой он находится,
- его временной зоне,
- а также о значении температуры (как она ощущается).

Значение временной зоны выводить в формате UTC±N, где N - цифра временного сдвига.
Протестировать выполнение программы со следующими городами: Чикаго, СПб, Дакка.

Пример вызова функции и получаемого результата.

```python
get_weather_data('Kiev', api_key=key)
>>> {"name": "Kyiv", "coord": {"lon": 30.52, "lat": 50.43}, "country": "UA", "feels_like": 21.96, "timezone": "UTC+3"}

```

При реализации программы, не публикуйте свой ключ для осуществления запросов. Сразу же после создания борда в реплите, используйте вкладку слева "secrets"), а при публикации кода в гитхабе — исключите из коммитов подключаемый файл, где разместите ключ, с помощью ```.gitignore```.
Для организации запросов используйте модуль ```requests```. Для кодирования и декодирования ```json``` - одноименный модуль.

Ссылка про secrets: https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables
=======
# Лабораторная работа 2, Яблонская Евгения

Результат:
![image](https://github.com/user-attachments/assets/e062506a-ac32-4e6c-a1b8-b2a74aedbfec)

Результат тестирования:
![image](https://github.com/user-attachments/assets/827e55ff-a25b-4d0e-992b-f5cd2245a894)

Код программы:

```

from owm_key import owm_api_key
import requests
from tabulate import tabulate


def get_weather_data(place, api_key=None):
    if api_key is None or len(place) < 2:
        return None

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')

    res_obj = res.json()

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

```
>>>>>>> 068b773d8feecde9f19b36ef960aca52e357cf07
