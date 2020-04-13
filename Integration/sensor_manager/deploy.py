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
	user_id = input('Enter User ID : ')
	service_id = input('Service ID ')
	query = str(input('Config Path : '))
	# Query-> sensor_name:Fan   

	# Make Request To Sensor Manager To Get Sensor Topics  
	URL = "http://127.0.0.1:5040/"
	para = {'data' : user_id + ' ' + service_id + ' ' + query}

	response = requests.post(url=URL, params = para )

	topic = response.json()['topic']
	if(topic == 'False' or topic == 'None'):
		print("Not Autho")
	else:
		print('Sensor topic : ' + topic)
		get_sensor_data(topic)

if __name__ == '__main__':
	main()