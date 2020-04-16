import requests
import flask
import json
import threading
from flask import request

app = flask.Flask(__name__)
port = 9000
	
@app.route('/servicelcm/service/deploymentStatus', methods=['POST'])
def deploymentStatus():
	req = request.get_json()
	print(req)
	res = {'status' : 'ok'}
	return flask.jsonify(res)

app.run(port = 9000)

