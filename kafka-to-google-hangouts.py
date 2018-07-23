#!/usr/bin/env python

"""This script pulls the messages from Kafka with specific topic(s) and push them to Google Hangouts webhook.
"""

import ConfigParser
import logging
import multiprocessing
import threading
import time

from json import dumps
from httplib2 import Http
from kafka import KafkaConsumer

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

KAFKA_ENDPOINT = '{0}:{1}'.format(config.get('Kafka', 'kafka_endpoint'), config.get('Kafka', 'kafka_endpoint_port'))
KAFKA_TOPIC = config.get('Kafka', 'topic')

WEBHOOK_URL = config.get('Hangouts', 'webhook_url')
MESSAGE_HEADERS = {'Content-Type': 'application/json; charset=UTF-8'}


class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()
        
    def stop(self):
        self.stop_event.set()
        
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=KAFKA_ENDPOINT,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        consumer.subscribe([KAFKA_TOPIC])
        
        while not self.stop_event.is_set():
            for consumer_record in consumer:
                bot_message = {'text' : consumer_record.value}
                http_obj = Http()
                response = http_obj.request(
                    uri=WEBHOOK_URL,
                    method='POST',
                    headers=MESSAGE_HEADERS,
                    body=dumps(bot_message),
                )
                print(response)

                if self.stop_event.is_set():
                    break
        
        
def main():
    tasks = [
        Consumer()
    ]

    for t in tasks:
        t.start()
        
        
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
