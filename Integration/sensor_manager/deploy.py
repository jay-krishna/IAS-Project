import requests
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer

def get_sensor_data(topic):
	consumer = KafkaConsumer(topic,bootstrap_servers=['localhost:9092'],auto_offset_reset = "latest")

	for message in consumer:
		s = message.value.decode('utf-8')
		print(s)

def main(): 

	# Make Request To Sensor Manager To Get Sensor Topics  
	file=open("config.json","r")
	data=json.load(file)

	d = {"username":"pratik","application_name":"application1","service_name":"service-1","unique_id":"pratik_application1_service-1","config_file":data}
	r=requests.post(url="http://127.0.0.1:5040/",json=d)

	# topic = r.json()
	# print(topic)
	# if(topic == 'False' or topic == 'None'):
	# 	print("Not Autho")
	# else:
	# 	print('Sensor topic : ' + topic)
	# 	get_sensor_data(topic)

if __name__ == '__main__':
	main()