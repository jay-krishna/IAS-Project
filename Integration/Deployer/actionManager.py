import flask
import json
import threading
from flask import request

app = flask.Flask(__name__)
port = 7000

@app.route('/actionmanager', methods=['POST'])
def getTopic():
	req = request.get_json()
	print(req)
	res = {
		"status" : 200
	}	
	return flask.jsonify(res)

app.run(port = port)
