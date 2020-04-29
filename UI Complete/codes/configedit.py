import requests
import json

def FetchServices(username):
	services=["Application-1_Service-1","Application-1_Service-2","Application-2_Service-1","Application-2_Service-2"]

	return services

def FetchSensorTypes(username):
	d = {'username':username}
	r=requests.post(url="http://127.0.0.1:5051/getsensordata",json=d)
	data=r.json()["data"]

	return list(data.keys())

def FetchSensorLocations(username,loc):
	d = {'username':username}
	r=requests.post(url="http://127.0.0.1:5051/getsensordata",json=d)
	data=r.json()["data"][loc]
	send=[]
	for _ in data:
		send.append(_["area"]+"_"+_["building"]+"_"+_["room_no"])
	return send