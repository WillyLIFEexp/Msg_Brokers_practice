import pika
import time
import logging
logging.basicConfig(level=logging.INFO)

def send_greet_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', port=5672)
    )
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')
    message = 'Hello World!'
    logging.info('-'*30)
    for i in range(5):
        logging.info('')
    logging.info('Pushing data to queue')
    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    for i in range(5):
        logging.info('')
    logging.info('-'*30)
    connection.close()

if __name__ == "__main__":
    send_greet_message()