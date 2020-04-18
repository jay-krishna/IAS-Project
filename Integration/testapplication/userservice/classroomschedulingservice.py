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
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	consumer = KafkaConsumer(str(temp_topic),bootstrap_servers=['127.0.0.1:9092'],auto_offset_reset = "latest")
	
	for message in consumer:
		s = message.value.decode('utf-8')

		temp = s.split()
		x = temp[1]
		y = temp[2]

		print('Msg Proff : ' + str(x))
		print('Msg Acad Office : ' + str(y))
			


if __name__ == '__main__':
	main()
