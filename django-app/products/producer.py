import pika



cloud_url = "amqps://grwcxnpd:riS-NtEcw-u317IJw8fESetC6FbJRtCN@mustang.rmq.cloudamqp.com/grwcxnpd"
params = pika.URLParameters(cloud_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='main',body='hello')
