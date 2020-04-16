import requests
import flask
import json
import threading
from flask import request



def sendRequest():
	URL = "http://localhost:5050/deploymentManager/deploy"
	machine_username = 'dharmesh'
	machine_password = 'root'
	ip = '127.0.0.1'
	port = 8000
	uname = 'dhamo'
	application_name = 'Application-1'
	service_name = 'service1'
	service_id = uname+"_"+application_name+"_"+service_name
	dependency=['service1','service2']

	req = {
		'machineusername' : machine_username,
		'password' : machine_password,
		'serverip' : ip,
		'sshport' : port,
		'username' : uname,
		'applicationname' : application_name,
		'servicename' : service_name,
		'serviceid' : service_id,
		
	}
	requests.post(url = URL, json = req)

sendRequest()
