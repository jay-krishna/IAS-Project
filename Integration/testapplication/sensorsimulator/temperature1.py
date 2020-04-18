from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import time
import random
import threading 


def sensor():
	producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
	while True:
		n = random.randrange(10,500)
		msg = 'nilgiri_roomno:100' +  ' ' + str(n)
		producer.send(str('temperature1_out'), bytes(str(msg),"utf-8"))
		producer.flush() 
		time.sleep(2)

def main():
	t1 = threading.Thread(target=sensor, args=())
	t1.start()
	consumer = KafkaConsumer('temperature1_in',group_id='doorstep1',bootstrap_servers=['127.0.0.1:9092'])
	for message in consumer:
		msg = message.value.decode('utf-8')
		print("Message recv ",msg)

main()
