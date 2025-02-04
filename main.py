from weather import Weather
import streamlit as st
import pandas as pd

api_key = st.secrets['API_KEY']


st.title("My Weather app")
st.subheader("Enter the name of the city:")


with st.form(key="City name"):
    user_input = st.text_input("City name:", placeholder="Type city name here")
    submit_button = st.form_submit_button(label="Submit")


# Button to submit input
if submit_button:
    # Pass the user input to the function and display the result
    if user_input:
        lat, lon = Weather.get_one_call_weather(user_input, api_key)
        if lat and lon:
            # Display a map centered at the city
            st.subheader(f"Location of {user_input.capitalize()}:")
            city_location = pd.DataFrame({"lat": [lat], "lon": [lon]})
            st.map(city_location)
    else:
        st.warning("Please enter a valid name!")


