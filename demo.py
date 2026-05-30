# City namedata['name']
# Temperaturedata['main']['temp']
# Feels likedata['main']['feels_like']
# Humiditydata['main']['humidity']
# Descriptiondata['weather'][0]['description']
# Wind speeddata['wind']['speed']



reading = {'coord': {'lon': 80.9167, 'lat': 26.85}, 
           'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}], 
           'base': 'stations', 
           'main': {'temp': 302.14, 'feels_like': 304.32, 'temp_min': 302.14, 'temp_max': 302.14, 'pressure': 1005, 'humidity': 61, 'sea_level': 1005, 'grnd_level': 991}, 
           'visibility': 5000, 
           'wind': {'speed': 4.12, 'deg': 60}, 
           'clouds': {'all': 40}, 'dt': 1780157147, 
           'sys': {'type': 1, 'id': 9176, 'country': 'IN', 'sunrise': 1780098201, 'sunset': 1780147479}, 
           'timezone': 19800, 'id': 1264733, 'name': 'Lucknow', 'cod': 200}


print(f"City - {reading['name']}")
print(f"Temp - {reading['main']['temp']-273.15:0.2f}C")
print(f"Feels - {reading['main']['feels_like']-273.15:0.2f}C")
print(f"Humidity - {reading['main']['humidity']}")
print(f"Wind Speed - {reading['wind']['speed']}")
print(f"Description -- {reading['weather'][0]['description']}")