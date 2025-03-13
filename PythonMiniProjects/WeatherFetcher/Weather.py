# a program that fetches and displays weather information for a given location.

import requests

def get_weather(city_name, api_key):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        weather_info = {
            'city': city_name,
            'temperature': main['temp'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed'],
            'conditions': weather['description']
        }
        return weather_info
    else:
        return None


if __name__ == "__main__":
    api_key = '******************************'
    city_name = input("Enter city name: ")

    weather_data = get_weather(city_name, api_key)

    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Conditions: {weather_data['conditions']}")
    else:
        print("City not found or API error.")
