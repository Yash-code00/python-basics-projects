import requests
api_key='737b0b46135d75c47bb814b9b3af0ccd'
city_name = input("enter the city: ")
def weather():
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json() 
    temp_k = data['main']['temp']
    feels_like_k = data['main']["feels_like"]
    feels_like_c = feels_like_k - 273.15
    temp_c = temp_k - 273.15   
    if response.status_code == 200:
        print(f"name: {data['name']}")
        print(f"weather: {data['weather'][0]['description']}")
        print(f"temp: {temp_c:.2f} celcius")
        print(f"feels_like: {temp_c:.2f} celcius")
        print(f"humidity: {data['main']['humidity']}")
    else:
        return False

print(weather())

#output
"""
name: Mumbai
weather: haze
temp: 34.99 celcius
feels_like: 314.6
humidity: 52
"""
