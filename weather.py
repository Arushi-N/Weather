import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

city = input("Enter the city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key=8bd53dfaf2924ea784e184407261302&q={city}"

r = requests.get(url, verify=False)

data = r.json() 

print(f"The temperature in {city} is: {data['current']['temp_c']}°C")