import time
import sys
from kafka import KafkaConsumer
from kafka import KafkaProducer

sensor_topic = sys.argv[1]
output_topic = sys.argv[2]
service2_topic = sys.argv[3]
service2_topic = sys.argv[4]
consumer = KafkaConsumer(sensor_topic,bootstrap_servers=['172.17.0.1:9092'])
producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9092'])
print("consuming started")
for message in consumer:
   print(message.value.decode('utf-8'))
   producer.send(output_topic, message.value)        

