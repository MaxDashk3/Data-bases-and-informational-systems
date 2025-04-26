 
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
channel = "messages_channel"

username = input("Enter your username: ")

while True:
    msg = input('> ')
    if msg!="":
        msg = f"{username}: {msg}"
        r.publish(channel, msg)
