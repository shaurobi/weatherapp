__author__ = 'shaurobi'

import sys
import json
import requests

web = "http://api.openweathermap.org/data/2.5/weather?"
key = "83fcd7c8d13fa1ebfa85e29312efa126"
city = "Sydney"

#build URL request from above variables
url = web + "q=" + city + "&APPID=" + key + "&units=metric"

#pull response from url
value = requests.get(url)

#print status code from request -- 200 means it worked!
print(value.status_code)

#print the main temp
currenttemp = value.json()['main']['temp']
print currenttemp

#call("+61431155901", {"network":"SMS"})
#say("The current weather in Sydney is
