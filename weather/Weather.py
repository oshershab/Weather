import requests
from datetime import datetime
import streamlit as st


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
        "units": "metric",
        "exclude": "minutely",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        # print the time of requested city
        unix_timestamp = data['current']['dt']
        time = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        st.subheader(f"Current Weather in {city_name.capitalize()}:")
        st.write(f"**Current Time:** {time}")

        # Display the temperature and conditions
        st.write(f"**Temperature:** {data['current']['temp']}°C")
        st.write(f"**Feels Like:** {data['current']['feels_like']}°C")
        st.write(f"**Humidity:** {data['current']['humidity']}%")
        st.write(f"**Weather Description:** {data['current']['weather'][0]['description'].capitalize()}")
        # Return coordinates for the map
        return lat, lon
    else:
        st.error(f"Error: {data['message']}")
        return None, None


