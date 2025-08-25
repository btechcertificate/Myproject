# from kombu import Connection, Exchange, Producer
# from kombu.exceptions import KombuError
# import json

# RABBIT_URL = 'amqp://guest:guest@localhost:5672//'

# order_exchange = Exchange('product_creation_events', type='direct', durable=True)


# # Persistent Connection Producer Setup
# # Instead of opening/closing a connection for every publish, we keep one alive.
# # This is more efficient for high-throughput systems.


# class RabbitMQPublisher:
#     def __init__(self):
#         self.connection = None
#         self.producer = None
#         self._connect()

#     def _connect(self):
#         try:
#             self.connection = Connection(RABBIT_URL, heartbeat=10)
#             self.connection.connect()
#             self.producer = Producer(self.connection)
#             print("✅ Connected to RabbitMQ")
#         except KombuError as e:
#             print(f"RabbitMQ connection failed: {e}")
#             self.connection = None
#             self.producer = None

#     def publish_order_event(self, product_name):
#         # WE can also make it generic to publish any event
#         # and put the meesage creation part in seperate file like event.py with publish_order_event
#         # but for now we are writting function definition here
#         if not self.producer:
#             self._connect()

#         if not self.producer:
#             # Could not connect, return failure
#             print("RabbitMQ still down. Event not sent.")
#             return False

#         try:
#             message = {"product_name": product_name}
#             self.producer.publish(
#                 message,
#                 exchange=order_exchange,
#                 routing_key='product.create',
#                 serializer='json',
#                 declare=[order_exchange],
#                 delivery_mode=2  # persistent
#             )
#             print(f"📨 Sent event for product {product_name}")
#             return True
#         except KombuError as e:
#             print(f"Publish failed: {e}")
#             self.producer = None
#             return False


# # Create one global instance
# rabbitmq_publisher = RabbitMQPublisher()
