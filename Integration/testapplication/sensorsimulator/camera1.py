from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import time
import random
import threading 

def sensor_1():
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
	n = random.randrange(10,100)
	while True:
		print("Number of people in room 100 ",n)
		producer.send(str('camera1_out'), bytes(str(i),"utf-8"))
		producer.flush() 
		time.sleep(2)

def main():
	t1 = threading.Thread(target=sensor_1, args=())
	t1.start()
	consumer = KafkaConsumer('camera1_in',group_id='camera1',bootstrap_servers=['localhost:9092'])
	for message in consumer:
		print("Message recv from instance ",message.value.decode('utf-8'))

main()
