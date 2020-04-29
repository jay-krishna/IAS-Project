from flask import Flask, request, jsonify
import os
import requests
import json

app = Flask(__name__)

@app.route("/getsensordata",methods=['POST'])
def getsensordata():
	data=request.get_json()
	print(data)

	file=open("data.json","r")
	data=json.load(file)

	return jsonify({"data":data})

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True,port=5051) 