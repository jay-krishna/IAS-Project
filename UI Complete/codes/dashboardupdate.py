import requests
import json

def update(username):
	params = dict()
	params["username"] = username
	r=requests.post("http://127.0.0.1:5056/req",json=params)
	data=r.json()
	send_data=[]
	print(data)
	for app in data:
		# print(app)
		app_name=app["appname"]
		for _ in app["data"]:
			# print(_)
			send_data.append([app_name,_["servicename"],_["status"],_["scheduled"],_["serviceid"]])

	return send_data
