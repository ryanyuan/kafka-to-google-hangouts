#!/usr/bin/env python
import ConfigParser
import logging
import multiprocessing
import threading
import time

from json import dumps
from httplib2 import Http

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

WEBHOOK_URL = config.get('Hangouts', 'webhook_url')
MESSAGE_HEADERS = {'Content-Type': 'application/json; charset=UTF-8'}
MESSAGES = ['Hello worlds!', 'This is a Google Hangouts test.', 'Developered by Ryan Yuan']
        
def main():
    for msg in MESSAGES:
        bot_message = {'text' : msg}
        http_obj = Http()
        response = http_obj.request(
            uri=WEBHOOK_URL,
            method='POST',
            headers=MESSAGE_HEADERS,
            body=dumps(bot_message),
        )
        print response
        
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
