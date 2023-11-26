import requests

def get_weather(city_name):
    api_key = '2f44ab8d94825710392977b37c24d3ac'

    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'Temperature': data['main']['temp'],
            'Humidity': data['main']['humidity'],
            'Precipitation': data['weather'][0]['description'],
            'Pressure': data['main']['pressure'],
            'Wind': {
                'Speed': data['wind']['speed'],
                'Direction': data['wind']['deg']
            }
        }
        return weather
    else:
        return None


city_name =str(input("Enter the city name:"))
weather_data = get_weather(city_name)

if weather_data:
    print(f"The weather in {city_name} is as follows:")
    print(f"Temperature: {weather_data['Temperature']}°C")
    print(f"Humidity: {weather_data['Humidity']}%")
    print(f"Precipitation: {weather_data['Precipitation']}")
    print(f"Pressure: {weather_data['Pressure']} hPa")
    print(f"Wind Speed: {weather_data['Wind']['Speed']} m/s")
    print(f"Wind Direction: {weather_data['Wind']['Direction']}°")
else:
    print("Failed to fetch weather data")
