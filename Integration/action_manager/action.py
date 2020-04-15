from flask import Flask ,jsonify,request
import json
from pymongo import MongoClient
import threading
from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
import hashlib

registry_ip = 'localhost'
registry_port = 27017
sensor_client = 'final3'
sensor_document = 'sensor'
kafka_platform_ip = 'localhost:9092'

app = Flask(__name__)
	

def send_data_to_sensor(host_topic,service_id):
	
	
	consumer = KafkaConsumer(str(service_id),group_id='action_module',bootstrap_servers=[kafka_platform_ip],auto_offset_reset = "latest")
	
	for message in consumer:
		s = message.value.decode('utf-8')
		print('Some Output generated')
		for i in host_topic:
			ip,topic = i.split(' ')
			producer = KafkaProducer(bootstrap_servers=[ip])
			producer.send(topic, bytes(s,"utf-8"))    
			producer.flush()
			time.sleep(1)
		
		time.sleep(2)

@app.route('/' ,methods=['GET' ,'POST'])
def fun():

	#get userid , config file as a request
	data = request.args.get('data')
	data = data.split()
	user_id = data[0]
	service_id = data[1]
	config_path = data[2]

	sensor_host = request.args.get('sensor_host')
	host_topic = json.loads(sensor_host)
	#dump file into json

	# print(sensor_host_list)
	d=None
	with open(config_path) as f:
		d = json.load(f)

	#store each query in a list	
	query=[]
	for i in d:
		query.append(d[i])

	for i in query:
		if(i['send_data_to_sensor'] == "True"):
			t = threading.Thread( target = send_data_to_sensor, args=(host_topic,service_id,))
			t.start()

		if(i['Output_display_to_user'] != "None"):
			t = threading.Thread( target = Output_display_to_user, args=(i['Output_display_to_user'],service_id,))
			t.start()

	# send temp topic to deployer
	temp = {'ack': 'OK'}
	return temp

if __name__ == '__main__':
   app.run(debug=True,port=5080)