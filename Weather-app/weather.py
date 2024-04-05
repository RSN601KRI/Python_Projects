import requests

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '72f9f9d278eecc04139afb525c03b7c4'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def main():
    print("Welcome to the Weather App!")
    city = input("Enter the city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Weather data not available for the entered city.")

if __name__ == "__main__":
    main()
