from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9092'])
i = 0
while True:
	producer.send("topic1",("sensor 1 : " + str(i)).encode("utf-8"))
	time.sleep(1)
	i += 1
