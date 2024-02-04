import requests

api_key = '97f4ea9dc183ab1e61bb6afcc2cb2a01'

user_input = input("Enter City: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']

temp = weather_data.json()['main']['temp']
temp = int(((temp) - 32) * 5/9)

a = weather_data.json()["main"]["feels_like"]
a = int(((a) - 32) * 5/9)
print(f"Feels Like: {a} degree celcius")
b = weather_data.json()["main"]["temp_min"]
b = int(((b) - 32) * 5/9)
print(f"Minimum Temperature: {b}")
c = weather_data.json()["main"]["temp_max"]
c = int(((c) - 32) * 5/9)
print(f"Maximum Temperature: {c}")
d = weather_data.json()["main"]["humidity"]
print(f"Humidity: {d}")

print(f"Temperature: {temp}")
print(f"Weather Description: {weather}")


#print(weather_data.json())