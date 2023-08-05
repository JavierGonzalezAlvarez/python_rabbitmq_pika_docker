import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='queue')

    def callback(ch, method, properties, body):
            print("\nReceived: ")
            print(body)

    channel.basic_consume(queue='queue', on_message_callback=callback, auto_ack=True)

    print(' -- Waiting for messages. CTRL+C to exit')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)