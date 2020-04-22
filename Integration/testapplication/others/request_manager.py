from flask import Flask,request,jsonify
import requests
import json

def main():

	
	# file=open("sensorregistration.json","r")
	# data=json.load(file)
	# d = {'username':'ias11','config_file':data}
	# r=requests.post(url="http://127.0.0.1:5051/sensorregistration",json=d)
	

	# d= {'value':'max'}
	# r=requests.post(url="http://127.0.0.1:9000/temperature1",json = d)
	
	d = {'username':'ias11'}
	r=requests.post(url="http://127.0.0.1:5050/getsensordata",json=d)
	# r=requests.post(url="http://127.0.0.1:5000/getsensordata",json=d)
	d = r.json()
	print(d)
	# return 200
	
if __name__ == '__main__':
	main()
