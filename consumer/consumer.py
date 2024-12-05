import pika
import time
import logging
logging.basicConfig(level=logging.INFO)

def receive_message():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq', port=5672)
                )
            channel = connection.channel()
            break
        except pika.exceptions.AMQPConnectionError:
            logging.warning("Waiting for RabbitMQ...")
            time.sleep(5)

    channel.queue_declare(queue='test_queue')

    def callback(ch, method, properties, body):
        logging.info(f" [x] Received {body.decode()}")

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    logging.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    receive_message()