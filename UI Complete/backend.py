from flask import Flask,request,jsonify,redirect
from flask import render_template
import requests
import json

sensorname = None

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
			sensorname=["one","two","three","four"]
			return render_template('/query/query.html',user=username,sensors=sensorname,displaytext=None)
		else:
			selected_sensorname=request.form["sensorname"]
			querytype=request.form["querytype"]
			return render_template('/query/query.html',user=None,sensors=sensorname,displaytext=querytype+" is : 32")

	return render_template('/query/query.html',user=None,sensors=None,displaytext=None)



if __name__ == "__main__":
    app.run(debug=True,port=6060) 