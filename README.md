Weather App: 🌦️
This project is a Streamlit-based Weather App that provides real-time weather information for any city using the OpenWeather API. The app displays current weather details such as temperature, humidity, and weather description. The app retrieves data based on the city name provided by the user and presents the information in a simple and interactive web interface.

Project structure:
Weather
|_ test
|_ weather
	|_ __init__.py
	|_ weather.py # Contains the weather-fetching logic
  
|__ main.py      # Main Streamlit app file to run the app
|__ README.md    # Documentation for the project
|__ poetry.lock	 # Poetry lock file with dependencies
|__ pyproject.toml # Poetry configuration file
|__ requirements.txt


Features:
Provides real-time weather information:
Current Time (based on UTC)
Temperature (°C)
Feels Like temperature (°C)
Humidity (%)
Weather Description (e.g., "Clear Sky", "Light Rain")
Simple and interactive UI using Streamlit.
User-friendly city input form with submission handling.

Usage:
Enter the name of the city in the input form (e.g., "New York", "Tel Aviv").
Press the Submit button.
The weather information for the requested city will be displayed, including:
Current time in UTC
Temperature (in Celsius)
Feels like temperature
Humidity percentage
Weather condition (e.g., cloudy, sunny)

Prerequisites:
Python (>= 3.7)
Poetry for dependency management. Install it via:
bash
Copy code
pip install poetry

Setup Instructions
1. Clone the Repository
bash
Copy code
git clone <your-repo-url>
cd <your-repo-folder>
2. Install Dependencies with Poetry
Run the following command to install dependencies:

bash
Copy code
poetry install
This will install packages defined in pyproject.toml.

3. Create a Secret Configuration
To securely store your API key, create a file named .streamlit/secrets.toml in the root directory:

bash:
mkdir -p .streamlit
Then add the following content:

toml:
[API_KEY]
API_KEY = "YOUR_OPENWEATHER_API_KEY"
4. Activate the Poetry Shell
Start a Poetry shell environment:

bash:
poetry shell
How to Run the Application
Open your terminal and navigate to the project folder.
Run the Streamlit app with:
bash:
streamlit run main.py

The app will open automatically in your browser

or open:
https://weather-samvtei2ipaal5cmy3wwtq.streamlit.app/


File Descriptions:
1. weather.py
This file contains the function get_one_call_weather(), which:

Converts the city name to latitude and longitude using OpenWeather's Geo API.
Calls OpenWeather's One Call API to fetch current weather details.
Displays the weather information using Streamlit components such as st.subheader(), st.write(), and st.error().

2. main.py
This is the main script to run the Streamlit app. It:

Displays the app title and input form.
Captures the user's input and calls the function from weather.py.
Handles form submission and error handling for invalid inputs.