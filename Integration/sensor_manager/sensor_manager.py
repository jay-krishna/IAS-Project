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

def dump_data(ip,topic ,service_id ,sensor_id ,rate): 

	producer = KafkaProducer(bootstrap_servers=[kafka_platform_ip])
	consumer = KafkaConsumer(str(topic),bootstrap_servers=[ip],auto_offset_reset = "latest")
	
	for message in consumer:
		s = message.value.decode('utf-8')
		s = s + ":" + sensor_id
		
		producer.send(service_id, bytes(s,"utf-8"))    
		producer.flush()
		time.sleep(rate)

def sensor_topic_binding_to_tempTopic(sensor_topic,host_topic,service_id ,data_rate):

	for i in range(len(sensor_topic)):
		temp = sensor_topic[i].split(' ')
		ip = temp[0]
		topic=temp[1]
		sensor_id = host_topic[i]
		t= threading.Thread(target=dump_data ,args=(ip,topic ,service_id,sensor_id,data_rate[i] ,))
		t.start()
		
		
def authorization(query,user_id):
	client = MongoClient(registry_ip ,registry_port)

	mydb = client[sensor_client]
	mycol = mydb[sensor_document]

	result=[]
	for i in range(len(query)):

		docs = mycol.find(query[i])
		for j in docs:
			
			if(j['user_id'] == user_id):
				continue
			else:
				return 'False'
		
		result.append(list(docs))

	if(len(result) == 0):
		print(len(result))
		return 'NM'

	return 'True'


def resolver(query):
	client = MongoClient('localhost' ,27017)

	mydb = client[sensor_client]
	mycol = mydb[sensor_document]

	# my_query = {'user_id':user_id ,q1:q2}
	sensor_topic = []
	host_topic=[]
	for i in range(len(query)):
		docs = mycol.find(query[i])
		for j in docs:
			# if('kafka' in j['data_dump']):
			sensor_topic.append(j['data_dump']['kafka']['broker_ip'] + " " + j['data_dump']['kafka']['topic'])
			host_topic.append(j['sensor_host']['kafka']['kafka_broker_ip'] + " " + j['sensor_host']['kafka']['kafka_topic'])
	
	return sensor_topic,host_topic

@app.route('/' ,methods=['GET' ,'POST'])
def fun():

	#get userid , config file as a request
	data = request.args.get('data')
	data = data.split()
	user_id = data[0]
	service_id = data[1]
	config_path = data[2]
	
	#dump file into json
	d=None
	with open(config_path) as f:
		d = json.load(f)

	#store each query in a list	
	query=[]
	data_rate = []
	for i in d:
		data_rate.append(d[i]['processing']['data_rate'])
		print(d[i]['processing']['data_rate'])
		removed_value = d[i].pop('processing')
		query.append(d[i])

	# check authorization
	r = authorization(query,user_id) 
	if(r == 'False'):
		temp = {'topic':'False'}
		return temp,200
	elif(r=='NM'):
		temp = {'topic':'None'}
		return temp


	#get sensor topic and host topic
	sensor_topic,host_topic = resolver(query)
	
	# create temp topic
	# # Open thread for execution
	t = threading.Thread( target = sensor_topic_binding_to_tempTopic , args=(sensor_topic,host_topic,service_id,data_rate,) )
	t.start()

	# send temp topic to deployer
	temp = {'topic': service_id}
	return temp

if __name__ == '__main__':
   app.run(port=5040)