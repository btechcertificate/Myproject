# producer.py
from kombu import Connection, Exchange, Queue, Producer
import product

# RabbitMQ connection
rabbit_url = "amqp://guest:guest@localhost:5672//"
connection = Connection(rabbit_url)

# Declare a durable direct exchange
exchange = Exchange('product_creation_events', type='direct', durable=True)

# Durable queue bound to the exchange
queue = Queue('product_created_queue', exchange, routing_key='product.create', durable=True)

def send_product_creation_event(product_name):
    # here we are every oopening a connection to RabbitMQ
    # that is not efficient, we should keep a persistent connection
    # in high throughput systems
    with connection:
        producer = Producer(connection)
        message = {"product_name": product_name}

        # Publish persistent message (delivery_mode=2)
        producer.publish(
            message,
            exchange=exchange,
            routing_key='product.create',
            declare=[exchange, queue],
            delivery_mode=2  # Persistent
        )
        print(f"Sent product name: {product_name}")
