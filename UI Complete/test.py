from flask import Flask,request,jsonify
import requests
import json

app = Flask(__name__)

@app.route("/recv",methods=['GET','POST'])
def receive():
	file=open("test.json","r")
	data=json.load(file)
	print("yes")
	return jsonify(data)


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True,port=7070) 