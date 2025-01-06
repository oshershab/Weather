from weather import Weather
import streamlit as st

api_key = st.secrets['API_KEY']


st.title("My Weather app")
st.subheader("Enter the name of the city:")


user_input = st.text_input("City name:", placeholder="Type city name here")


# Button to submit input
if st.button("Submit"):
    # Pass the user input to the function and display the result
    if user_input:
        checking_weather = Weather.get_one_call_weather(user_input, api_key)
    else:
        st.warning("Please enter a valid name!")