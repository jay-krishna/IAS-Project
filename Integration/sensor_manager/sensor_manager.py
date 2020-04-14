from flask import Flask ,jsonify,request
import json
from pymongo import MongoClient
import threading
from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
import hashlib
import random

registry_ip = 'localhost'
registry_port = 27017
sensor_client = 'final8'
sensor_document = 'sensor'
kafka_platform_ip = 'localhost:9092'

app = Flask(__name__)

def dump_data(ip,topic ,service_id ,sensor_id ,temptopic,rate): 

	producer = KafkaProducer(bootstrap_servers=[kafka_platform_ip])
	consumer = KafkaConsumer(str(topic),bootstrap_servers=[ip],auto_offset_reset = "latest")
	
	for message in consumer:
		s = message.value.decode('utf-8')
		s = s + ":" + sensor_id
		
		producer.send(temptopic, bytes(s,"utf-8"))    
		producer.flush()
		time.sleep(rate)

def sensor_topic_binding_to_tempTopic(sensor_topic,host_topic,service_id,temptopic,data_rate):

	for i in range(len(sensor_topic)):
		temp = sensor_topic[i].split(' ')
		ip = temp[0]
		topic=temp[1]
		sensor_id = host_topic[i]
		t= threading.Thread(target=dump_data ,args=(ip,topic ,service_id,sensor_id,temptopic,data_rate[i] ,))
		t.start()
		

def resolver(query,username):
	client = MongoClient('localhost' ,27017)

	mydb = client[sensor_client]
	mycol = mydb[sensor_document]

	# my_query = {'user_id':user_id ,q1:q2}
	sensor_topic = []
	host_topic=[]
	for i in range(len(query)):
		docs = mycol.find(query[i])
		for j in docs:
			if(j['user_id'] == username):
				sensor_topic.append(j['data_dump']['kafka']['broker_ip'] + " " + j['data_dump']['kafka']['topic'])
				host_topic.append(j['sensor_host']['kafka']['kafka_broker_ip'] + " " + j['sensor_host']['kafka']['kafka_topic'])
	
	return sensor_topic,host_topic


def filter(d):
	for i in d:
		if(d[i]['sensor_name'] == "None"):
			del d[i]['sensor_name']
		if(d[i]['sensor_geolocation']['lat'] == "None" or d[i]['sensor_geolocation']['long'] == "None"):
			del d[i]['sensor_geolocation']
		if(d[i]['sensor_address']['area'] == "None" or d[i]['sensor_address']['building'] == "None" or d[i]['sensor_address']['room_no'] == "None"):
			del d[i]['sensor_address']
	return d


# def checknearest(query,username):
	
# 	for i in range(len(query)):
# 		l = query[i].keys()
# 		if('sensor_geolocation' in l):
# 			lat = []

# 	return [1,2]



@app.route('/' ,methods=['GET' ,'POST'])
def fun():

	#get userid , config file as a request
	data = request.get_json()
	user_id = data['username']
	service_id = data['service_name']
	d = data['config_file']
	unique_id = data['unique_id']
	
	d=filter(d)

	#store each query in a list	
	query=[]
	data_rate = []

	for i in d:
		data_rate.append(d[i]['processing']['data_rate'])
		removed_value = d[i].pop('processing')
		query.append(d[i])

	#get sensor topic and host topic
	sensor_topic,host_topic = resolver(query,user_id)
	
	if(len(sensor_topic) == 0):
		# sensor_topic,host_topic = checknearest(query,user_id)
		# if(len(sensor_topic) == 0):
		temp = {'ack':'No Sensor Found or Not Authorized'}
		return temp
	
	print(sensor_topic)

	# create temp topic
	temptopic = unique_id + str(random.randrange(0,20))
	print(temptopic)
	Open thread for execution
	t = threading.Thread( target = sensor_topic_binding_to_tempTopic , args=(sensor_topic,host_topic,service_id,temptopic,data_rate,) )
	t.start()

	# send temp topic to deployer
	temp = {'ack': service_id}
	return temp

if __name__ == '__main__':
   app.run(debug=True,port=5040)