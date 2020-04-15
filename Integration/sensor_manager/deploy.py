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
	file=open("user_config.json","r")
	data=json.load(file)

	d = {"username":"pratik","applicationname":"application1","servicename":"fridge","serviceid":"pratik_application1_service-1","config_file":data}
	r=requests.post(url="http://127.0.0.1:5040/sensormanager",json=d)

	# topic = r.json()
	# print(topic)
	# if(topic == 'False' or topic == 'None'):
	# 	print("Not Autho")
	# else:
	# 	print('Sensor topic : ' + topic)
	# 	get_sensor_data(topic)

if __name__ == '__main__':
	main()