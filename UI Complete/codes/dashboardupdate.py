import requests
import json

def update():
	r=requests.get("http://127.0.0.1:7070/recv")
	data=r.json()
	send_data=[]
	for app in data:
		app_name=app["appname"]
		for _ in app["data"]:
			send_data.append([app_name,_["servicename"],_["status"],_["scheduled"],_["serviceid"]])

	return send_data