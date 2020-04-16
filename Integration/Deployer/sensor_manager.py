import flask
import json
import threading
from flask import request

app = flask.Flask(__name__)
port = 6000

@app.route('/sensormanager/', methods=['POST'])
def getTopic():
	req = request.get_json()
	print(req)
	res = {
		'temporary_topic' : 'topic1',
		'sensor_host' : ['sensor1_in', 'sensor2_in']
	}
	return flask.jsonify(res)

app.run(port = port)
