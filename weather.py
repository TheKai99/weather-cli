import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("OPEN_WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="



def check_city(city):

    url = f"{BASE_URL}{city}&appid={APP_ID}"

    response = requests.get(url)
    data = response.json()

    print("=============== Weather Report ==================")
    print(f"Place - {data['name']}")
    print(f"Temp - {data['main']['temp']-273.15:0.2f}C")
    print(f"Feels - {data['main']['feels_like']-273.15:0.2f}C")
    print(f"Humidity - {data['main']['humidity']}")
    print(f"Wind Speed - {data['wind']['speed']}")
    print(f"Description -- {data['weather'][0]['description']}")

