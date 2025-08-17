# 🌤️ Weather App in Python

A simple command-line Python program to fetch current weather information using the OpenWeatherMap API.

## Features

- Get current weather details for any city worldwide.
- Displays temperature, weather condition, humidity, and wind speed.
- Handles invalid city names and API errors gracefully.
- Easy-to-use command-line interface.

## Usage

1. Clone the repository or download the source code file.
2. Install the requests library if not already installed:
   ```bash
   pip install requests
3. Run the program with Python 3. For example:
   ```bash
   python weather_app.py
4. Enter a city name to get its weather or type exit to quit.

## Example

```
Welcome to the Weather App
Enter city name (or 'exit' to quit): London

Weather Information
-------------------
City: London, GB
Temperature: 18.5 °C
Condition: Clear sky
Humidity: 55%
Wind Speed: 3.4 m/s
```

## How the Program Works

- Uses the OpenWeatherMap API to fetch real-time weather data.
- API response is parsed to extract city, country, temperature, weather condition, humidity, and wind speed.
- Errors such as invalid city names or connection issues are handled gracefully.
- Loop continues until the user types exit.
   
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ggsurya/Python-Projects/blob/main/LICENSE) file for details.

## 📩 Contact

**G.G. Surya**  
📧 Email: ggsuryaff@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/g-g-surya-5aa9312b4)
🔗 [GitHub](https://github.com/ggsurya)
