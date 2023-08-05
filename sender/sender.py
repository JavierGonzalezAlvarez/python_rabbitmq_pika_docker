import pika

#Ensuring message delivery with the mandatory flag
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='queue', exclusive=False, auto_delete=False)

message_to_send = 'Send message to queue'

#Send to RabbitMQ
channel.basic_publish(exchange='', routing_key='queue', body=message_to_send)
print('Sent: ' + message_to_send)

connection.close()