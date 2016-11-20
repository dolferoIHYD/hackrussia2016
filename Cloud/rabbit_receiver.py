# coding: utf-8
import pika
import subprocess

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='tokens', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(queue=queue_name,exchange='tokens')

print ' [*] Waiting for messages. To exit press CTRL+C '

def callback(ch, method, properties, body):
    print ' [X] %r' % body
    subprocess.call('curl -X GET "0.0.0.0:80/api/" -d token={}'.format(body), shell=True)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
