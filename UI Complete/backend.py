from flask import Flask,request,jsonify,redirect
from flask import render_template
import os
import requests
import json

from codes import twowaysensor

sensorname = None

#change dest path
dest = "/home/pratik/"

app = Flask(__name__)

@app.route("/login",methods=['GET','POST'])
def login():
	return render_template('/login/login.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
	return render_template('/signup/signup.html')

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
	return render_template('/dashboard/dashboard.html')

@app.route("/output",methods=['GET','POST'])
def output():
	return render_template('/output/output.html')

@app.route("/sensor",methods=['GET','POST'])
def sensor():
	if(request.method == 'POST'):
		username = request.form["sensorregistration"]
		f = request.files['file']  
		f.save(os.path.join(dest, f.filename))

		jsonpath = dest+"sensor_registration.json"
		f = open (jsonpath, "r")

		config_data=json.load(f)

		reply = dict()
		reply["username"] = username
		reply["config_file"] = config_data
		req = requests.post(url="http://13.68.206.239:5051/sensorregistration",json=reply) 
		data = req.json()
		if(data['msg'] == 'Sensor Registered'):
			text = "sensors registered"
		else:
			text = "Some Error"
		os.system(f'rm {jsonpath}')
		return render_template('/sensor/sensor.html',displaytext=text)

	return render_template('/sensor/sensor.html')

@app.route("/application",methods=['GET','POST'])
def application():
	return render_template('/application/application.html')

@app.route("/query",methods=['GET','POST'])
def query():
	global sensorname
	if(request.method == 'POST'):
		if("username" in request.form.keys()):
			username=request.form["username"]
			sensorname = twowaysensor.getsensordata(username)
			return render_template('/query/query.html',user=username,sensors=sensorname,displaytext=None)
		else:
			selected_sensorname=request.form["sensorname"]
			querytype=request.form["querytype"]
			ans  = twowaysensor.getoutput(selected_sensorname,querytype)
			text="{} for {} is {}".format(querytype,selected_sensorname,ans)
			return render_template('/query/query.html',user=None,sensors=sensorname,displaytext=text)

	return render_template('/query/query.html',user=None,sensors=None,displaytext=None)



if __name__ == "__main__":
    app.run(debug=True,port=6060) 