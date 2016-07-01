import json
import requests

url = "https://api.ciscospark.com/v1/rooms"
key = "Bearer MGE4NTYzYTMtZmYzNi00Mzk4LTkyMGEtODgzZmNhYmVhYjJkZGRlYzI4NjctYjI3"

#pull response from url
payload = {'Authorization' : key}

value = requests.get(url, headers = payload)

#print status code from request -- 200 means it worked!
print(value.status_code)

#print the output
#print(value.json()['items']['title'])

dict = json.loads(value.text)
room_dict = dict
roomname = "Chester"
for room in room_dict['items']:
#print (room['title'])
	if (room['title']==roomname):
		print room['title']
