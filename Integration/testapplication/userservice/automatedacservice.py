from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import time
import random
import threading 
import sys

def main():
	temp_topic = sys.argv[1]
	output_topic = sys.argv[2]

	consumer = KafkaConsumer(str(temp_topic),bootstrap_servers=['127.0.0.1:9092'],auto_offset_reset = "latest")
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	for message in consumer:
		s = message.value.decode('utf-8')
		temprature = int(s.split()[1])
		msg = ''
		if int(temprature) >=10 and int(temprature)<=59:
			msg = msg + 'Low_Temp:' + str(temprature)
		elif int(temprature)>=60 and int(temprature)<=100:
			msg = msg + 'Normal_Temp:' + str(temprature)
		elif int(temprature)>=101 and int(temprature)<=120:
			msg = msg + 'High_Temp:' + str(temprature)

		print(msg)
		producer.send(str(output_topic), bytes(str(msg),"utf-8"))
		producer.flush() 
		time.sleep(1)
			

if __name__ == '__main__':
	main()