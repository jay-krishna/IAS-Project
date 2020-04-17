from flask import Flask,request,jsonify
import requests
import json

def main():

	
	# file=open("config.json","r")
	# data=json.load(file)
	# d = {'username':'pratik','config_file':data}

	d = {'username':'pratik'}
	r=requests.post(url="http://127.0.0.1:5050/getsensordata",json=d)
	# r=requests.post(url="http://127.0.0.1:5050/sensorregistration",json=d)
	d = r.json()
	print(d[0])
	
if __name__ == '__main__':
	main()