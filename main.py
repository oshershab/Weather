from weather import Weather

def main():
    api_key = "d3199210c072e0a333eacb3b62351047"
    city_name = input("Enter a city name: ")
    print(f"You entered: {city_name}")
    Weather.get_one_call_weather(city_name, api_key)


if __name__ == "__main__":
    main()

