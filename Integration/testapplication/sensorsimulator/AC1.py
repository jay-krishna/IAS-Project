from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import time
import random
import threading 

current_temperature = 20

def sensor():
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	while True:
		producer.send(str('AC1_out'), bytes(str(current_temperature),"utf-8"))
		producer.flush() 
		time.sleep(2)

def main():
	t1 = threading.Thread(target=sensor, args=())
	t1.start()
	consumer = KafkaConsumer('AC1_in',group_id='AC1',bootstrap_servers=['127.0.0.1:9092'])
	for message in consumer:
		msg = message.value.decode('utf-8')
		current_temperature = int(msg)
		print("Current Temperature in room 100",current_temperature)

main()
