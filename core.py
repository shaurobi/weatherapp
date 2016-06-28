__author__ = 'cobedien'


import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
url = "http://198.18.134.17/ins"
username = "admin"
password = "Cisco321"


payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show version',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))


kick_start_image = response.json()['result']['body']['kickstart_ver_str']
system_image = response.json()['result']['body']['kick_file_name']
host_name = response.json()['result']['body']['host_name']

payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show system resources',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))
cpu_state_idle=response.json()['result']['body']['cpu_state_idle']

print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('kickstart image version : ' + kick_start_image)
print ('system image version : ' + system_image)
if float(cpu_state_idle) > 68.00:
	print ('current idle cpu state: ' + cpu_state_idle)
print ("===============================")
