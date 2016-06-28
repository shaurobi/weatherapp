__author__ = 'shaurobi'

import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
# response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))


#kick_start_image = response.json()['result']['body']['kickstart_ver_str']
#system_image = response.json()['result']['body']['kick_file_name']
#payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show system resources',1], 'id': '1'}]
#my_data = json.dumps(payload)
#response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))
#cpu_state_idle=response.json()['result']['body']['cpu_state_idle']

web = "http://api.openweathermap.org/data/2.5/weather?"
key = "83fcd7c8d13fa1ebfa85e29312efa126"
city = "Sydney"

url = web + "q=" + city + "&APPID=" + key + "&units=metric"

value = requests.get(url)
print(value.status_code)
print(value.json()['main']['temp'])
test = value.json()
