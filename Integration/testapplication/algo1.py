import math
import sys
from random import random
from kafka import KafkaProducer
from kafka import KafkaConsumer

def readtemptopic(temp_topic,output_topic):
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	consumer = KafkaConsumer(topic,bootstrap_servers=['127.0.0.1:9092'],auto_offset_reset = "latest")

	for message in consumer:
		s = message.value.decode('utf-8')
		# format will be <roomno,numberofpeople>

		ans = PredictTemperature(int(s))
		
		#output will be <roomno,temperature>
		producer.send(output_topic, bytes(str(i),"utf-8"))
		producer.flush() 
		time.sleep(1)

def PredictTemperature(n_emp):
	mu=50
	temp0=25

	val_temp=(temp0-(-1*(n_emp-mu)**3)/5000)+random()/4
	if(val_temp>55):
		val_temp=random()+54.0
	if(val_temp<7):
		val_temp=random()+6.0
	
	return round(val_temp,2)


def main():
	temp_topic = sys.argv[1]
	output_topic = sys.argv[2]
	dependent_topic = sys.argv[3]

	readtemptopic(temp_topic,output_topic)


main()