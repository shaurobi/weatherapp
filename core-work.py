__author__ = 'shaurobi'

import sys
import json
import requests

web = "http://api.openweathermap.org/data/2.5/weather?"
key = "83fcd7c8d13fa1ebfa85e29312efa126"
city = "Sydney"

url = web + "q=" + city + "&APPID=" + key + "&units=metric"

value = requests.get(url)
print(value.status_code)
print(value.json()['main']['temp'])
test = value.json()
