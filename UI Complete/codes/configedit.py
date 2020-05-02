import requests
import json

def FetchServiceByApplication(username,application):
	if(application.split("_")[0]=="A1"):
		return ["A1_S1","A1_S2","A1_S3","A1_S4"]
	else:
		return ["A2_S1","A2_S2","A2_S3","A2_S4","A2_S5","A2_S6"]

def FetchServiceCount(username,application):
	return len(FetchServiceByApplication(username,application))

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
	# return ["A1_S1","A1_S2","A1_S3","A1_S4","A2_S1","A2_S2","A2_S3","A2_S4","A2_S5","A2_S6"]

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
