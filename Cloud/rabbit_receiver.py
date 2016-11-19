# coding: utf-8
import pika
import pycurl
import subprocess

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('0.0.0.0', 5672,)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='tokens', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(queue=queue_name,exchange='tokens')

print ' [*] Waiting for messages. To exit press CTRL+C '

def callback(ch, method, properties, body):
    print ' [X] %r' % body
    subprocess.call('curl -X GET "0.0.0.0:80" -d token={}'.format(body), shell=True)
    c = pycurl.Curl()
    c.setopt(c.URL, '0.0.0.0:80')
    c.setopt(c.WRITEDATA, body)
    c.perform()
    c.close()

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
