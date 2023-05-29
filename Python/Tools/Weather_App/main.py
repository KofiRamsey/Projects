import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

with open("api-key.txt", "r") as file:
    API_KEY = file.read().strip()
    
CITY = input('City: ').title()

def convert_temperature(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY

response = requests.get(url).json()

temperature_kelvin = response['main']['temp']
temperature_celcius, temperature_fahrenheit = convert_temperature(temperature_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celcius, feels_like_fahrenheit = convert_temperature(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f'The TEMPERATURE in {CITY} is: {temperature_celcius:.2f} `C')
print(f'The TEMPERATURE in {CITY} FEELS LIKE: {feels_like_celcius:.2f} `C')
print(f'The HUMIDITY in {CITY} is: {humidity}%')
print(f'The WIND SPEED in {CITY} is: {wind_speed}m/s')
print(f'The GENERAL WEATHER in {CITY} is: {description}')
print(f'The SUN RISES in {CITY} at {sunrise_time} local time')
print(f'The SUN SETS in {CITY} at {sunset_time} local time')
