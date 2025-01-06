import requests
from datetime import datetime


def get_one_call_weather(city_name, API_key, limit=1):
    # converting city name to lon and lat
    base_url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}"
    response_geo = requests.get(base_url_geo)
    data_geo = response_geo.json()[0]

    if response_geo.status_code == 200:
        lat = data_geo["lat"]
        lon = data_geo["lon"]
    else:
        print("failed to convert city to lat and lon")

    # getting weather information
    base_url = "https://api.openweathermap.org/data/3.0/onecall"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_key,
        "units": "metric",  # "metric" for Celsius, "imperial" for Fahrenheit
        "exclude": "minutely",  # You can exclude "minutely", "hourly", "daily", "alerts"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        # print the time of requested city
        unix_timestamp = data['current']['dt']
        time = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Current time in {city_name} is {time}")

        # print the temp of requested city
        print(f"Current tempeture in {city_name} is {data['current']['temp']}°C")

        # print weather conditions
        print(f"Current tempeture in {city_name} feels like {data['current']['feels_like']}°C")
        print(f"Current humidity in {city_name} is {data['current']['humidity']}%")



    else:
        print(f"Error: {data['message']}")
