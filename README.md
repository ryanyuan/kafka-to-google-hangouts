# Streaming messages from Apache Kafka to Google Hangouts bot

This project enables messages streaming process from [Apache Kafka](http://kafka.apache.org/) to [Google Hangouts bot](https://developers.google.com/hangouts/chat/quickstart/incoming-bot-python).

# Prerequisite

You need to have a running Kafka service.

# Environment configurations and validations

Open `config.cfg` and edit the values using text editor:

```
$ vim config.cfg
```

or 

```
$ nano config.cfg
```

Now let's check if `Producer` and `Consumer` are able to send and receive messages.

```
$ python kafka-test.py
...
ConsumerRecord(topic=u'mytopic', partition=1, offset=2244, timestamp=1532095366718, timestamp_type=0, key=None, value='test', checksum=None, serialized_key_size=-1, serialized_value_size=4)
ConsumerRecord(topic=u'mytopic', partition=1, offset=2245, timestamp=1532095366718, timestamp_type=0, key=None, value='\xc2Hola, mundo!', checksum=None, serialized_key_size=-1, serialized_value_size=13)
...
```

If you can see the above `ConsumerRecords`, then let's validate if Google Hangouts bot's webhook is running.

```
$ python hangouts-test.py
({'status': '200', 'content-length': '585', 'x-xss-protection': '1; mode=block', 'x-content-type-options': 'nosniff', 'transfer-encoding': 'chunked', 'vary': 'Origin, X-Origin, Referer', 'server': 'ESF', '-content-encoding': 'gzip', 'cache-control': 'private', 'date': 'Mon, 23 Jul 2018 06:27:01 GMT', 'x-frame-options': 'SAMEORIGIN', 'alt-svc': 'quic=":443"; ma=2592000; v="44,43,39,35"', 'content-type': 'application/json; charset=UTF-8'}, '{\n  "name": "spaces/AAAAXcBQUfE/messages/B-Jo5s-SKMA.B-Jo5s-SKMA",\n  "sender": {\n    "name": "users/114022495153014004089",\n    "displayName": "gcp-awesome-bot",\n    "avatarUrl": "",\n    "email": "",\n    "type": "BOT"\n  },\n  "text": "Hello worlds!",\n  "cards": [],\n  "previewText": "",\n  "annotations": [],\n  "thread": {\n    "name": "spaces/AAAAXcBQUfE/threads/B-Jo5s-SKMA"\n  },\n  "space": {\n    "name": "spaces/AAAAXcBQUfE",\n    "type": "ROOM",\n    "displayName": "GCP-POC"\n  },\n  "fallbackText": "",\n  "argumentText": "Hello worlds!",\n  "createTime": "2018-07-23T06:27:01.584735Z"\n}\n')
...
```

# Step-by-step

Now let's stream the messages from Kafka to Google Hangout bot.

```
$ python kafka-to-google-hangouts.py
...
({'status': '200', 'content-length': '681', 'x-xss-protection': '1; mode=block', 'x-content-type-options': 'nosniff', 'transfer-encoding': 'chunked', 'vary': 'Origin, X-Origin, Referer', 'server': 'ESF', '-content-encoding': 'gzip', 'cache-control': 'private', 'date': 'Mon, 23 Jul 2018 06:21:43 GMT', 'x-frame-options': 'SAMEORIGIN', 'alt-svc': 'quic=":443"; ma=2592000; v="44,43,39,35"', 'content-type': 'application/json; charset=UTF-8'}, '{\n  "name": "spaces/AAAAXcBQUfE/messages/sVjuLVzBTt4.sVjuLVzBTt4",\n  "sender": {\n    "name": "users/114022495153014004089",\n    "displayName": "gcp-awesome-bot",\n    "avatarUrl": "",\n    "email": "",\n    "type": "BOT"\n  },\n  "text": "@stories_startup Finally its for free https://t.co/ysIsYF4I3R",\n  "cards": [],\n  "previewText": "",\n  "annotations": [],\n  "thread": {\n    "name": "spaces/AAAAXcBQUfE/threads/sVjuLVzBTt4"\n  },\n  "space": {\n    "name": "spaces/AAAAXcBQUfE",\n    "type": "ROOM",\n    "displayName": "GCP-POC"\n  },\n  "fallbackText": "",\n  "argumentText": "@stories_startup Finally its for free https://t.co/ysIsYF4I3R",\n  "createTime": "2018-07-23T06:21:43.770383Z"\n}\n')
...
```

Congrats! Now the Kafka can stream the realtime message from Apache Kafka to Google Hangout bot.