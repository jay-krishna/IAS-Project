import requests
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer

def startalgo(topic):
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
	i= 0
	while True:
		producer.send(str('topic'), bytes('data' + str(i),"utf-8"))
		i=i+1
		producer.flush() 
		time.sleep(2)

def main():
	user_id = input('Enter User ID : ')
	service_id = input('Service ID ')
	query = str(input('Path to config :'))

	sensor_host = ['localhost:9092 sensor1_in','localhost:9092 sensor2_in']

	sensor_host = json.dumps(sensor_host)
	# print(sensor_host)
	# Make Request To Sensor Manager To Get Sensor Topics  
	URL = "http://127.0.0.1:5080/"
	para = {'data' : user_id + ' ' + service_id + ' ' +  query , 'sensor_host':sensor_host}

	response = requests.post(url=URL, params = para )

	ack = response.json()['ack']
	print(ack)
	# startalgo(service_id+'_out')

if __name__ == '__main__':
	main()