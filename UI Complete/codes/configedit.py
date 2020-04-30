import requests
import json

def FetchServices(username):
	params = dict()
	params["username"] = username
	req = requests.post(
				url="http://13.68.206.239:5056/getServiceList",
				json=params)
	response = req.json()
	services=response["services"]
	print("Received services = ",services)
	return services

def FetchSensorTypes(username):
	d = {'username':username}
	r=requests.post(url="http://127.0.0.1:5051/getsensordata",json=d)
	data=r.json()

	return list(data.keys())

def FetchSensorLocations(username,loc):
	d = {'username':username}
	r=requests.post(url="http://127.0.0.1:5051/getsensordata",json=d)
	data=r.json()[loc]
	send=[]
	for _ in data:
		send.append(_["area"]+"_"+_["building"]+"_"+_["room_no"])
	return send
