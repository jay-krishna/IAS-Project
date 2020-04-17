from flask import Flask,request,jsonify
import requests
import sys 
import json


@app.route('/createrequest' ,methods=['GET','POST'])
def fun():

	file=open("test_config.json","r")
	data=json.load(file)

	print(type(data))
	ack={'msg':'S'}
	return ack

if __name__ == '__main__':
   app.run(debug=True,port=sys.argv[1])