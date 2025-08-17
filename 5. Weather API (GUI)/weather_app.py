import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        if not response.text:
            print("Error: No response received from API.\n")
            return

        data = response.json()

        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unknown error')}\n")
            return

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print("\nWeather Information")
        print("-------------------")
        print(f"City: {city}, {country}")
        print(f"Temperature: {temp} °C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e, "\n")

def main():
    print("Welcome to the Weather App")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting...")
            break
        elif not city.strip():
            print("Please enter a valid city name.\n")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()
