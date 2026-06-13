# API (Application Programming Interface)
# request(so'rov) # response(javob)
# JSON (JavaScript Object Notation)
# HTTP request METHODS: get(olmoq), post(yubormoq), put/patch(yangilash), delete(o'chirish)
# API turlari
# 1. Public(ommaviy) APIs
# 2. Private(maxfiy, shaxsiy) APIs
# 3. Hamkorlik APIs

# requests library
import requests

from main import API_KEY
city_name = input("Xohlagan shahar nomini kiriting: ")
# Make a GET request
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={API_KEY}")
if response.status_code == 200:
    data = response.json()['main']['temp']
    print(f"Bugun {city_name}da {data} gradus ob-havo")
    # print(response.json())
else:
    print(f"Error: {response.status_code}")