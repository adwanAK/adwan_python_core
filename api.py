
import requests

from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b2175c44ff368c401ed884482283a418"
r = requests.get(url, json=True)

data = r.json()
pprint(data)
