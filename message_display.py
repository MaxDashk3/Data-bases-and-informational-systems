import redis, time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
channel = "messages_channel"
pubsub = r.pubsub()
pubsub.subscribe(channel)

for message in pubsub.listen():
    if message['type'] == 'message':
        print(message['data'])