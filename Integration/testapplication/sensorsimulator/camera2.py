from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import time
import random
import threading 

def sensor():
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	n = random.randrange(10,100)
	while True:
		print("Number of people in room 101 ",n)
		producer.send(str('camera2_out'), bytes(str(i),"utf-8"))
		producer.flush() 
		time.sleep(2)

def main():
	t1 = threading.Thread(target=sensor, args=())
	t1.start()
	consumer = KafkaConsumer('camera2_in',group_id='camera2',bootstrap_servers=['127.0.0.1:9092'])
	for message in consumer:
		print("Message recv from instance ",message.value.decode('utf-8'))

main()
