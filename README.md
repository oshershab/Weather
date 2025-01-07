# **Weather App 🌦️**

This project is a **Streamlit-based Weather App** that provides real-time weather information for any city using the **OpenWeather API**. The app displays current weather details such as temperature, humidity, and weather description. The app retrieves data based on the city name provided by the user and presents the information in a simple and interactive web interface.

---

## **Project Structure**



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



---

## **Features**

- Provides real-time weather information:
  - **Current Time** (based on UTC)
  - **Temperature** (°C)
  - **Feels Like** temperature (°C)
  - **Humidity** (%)
  - **Weather Description** (e.g., "Clear Sky", "Light Rain")
- Simple and interactive UI using **Streamlit**.
- User-friendly city input form with submission handling.

---

## **Usage Instructions**

1. Enter the **name of the city** in the input form (e.g., "New York", "Tel Aviv").
2. Press the **Submit** button.
3. The weather information for the requested city will be displayed, including:
   - Current time in UTC
   - Temperature (in Celsius)
   - Feels like temperature
   - Humidity percentage
   - Weather condition (e.g., cloudy, sunny)

---

## **Prerequisites**

- Python (>= 3.7)
- Poetry for dependency management. Install it via:
  ```bash
  pip install poetry


## **Setup Instructions**

### 1. **Clone the Repository**
To clone the project repository:
```bash
git clone <your-repo-url>
cd <your-repo-folder>
