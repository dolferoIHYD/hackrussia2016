# coding: utf-8
import pika
import sys

# подключение к брокеру на локалхост
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', 5672))
channel = connection.channel()

# Создание точки доступа с типом fanout и названием logs
# fanout - копирует сообщение во все очереди
channel.exchange_declare(exchange='tokens', type='fanout')

message = ' '.join(sys.argv[1:]) or 'aaa'
channel.basic_publish(exchange='tokens',
                        routing_key='',
                        body=message
                     )
print " [x] Sent %r" % (message,)

connection.close()
