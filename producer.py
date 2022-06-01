from time import sleep
from kafka import KafkaProducer
from data import get_register_data
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

'''def get_partition(key, all, avilable):
    return 0'''

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                            value_serializer = json_serializer)
                                            #,partitioner=get_partition)


if __name__ == "__main__":
    while 1==1:
        data = get_register_data()
        print(data)
        producer.send("first_demo", data)
        time.sleep(4)