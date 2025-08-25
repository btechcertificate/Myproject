# Here importing product model will not work because it's a normal script . it don't have idea about django ecosystem. 
# so ia m commenting this code and writting consumer in product/management/commands/product_consumer.py

# one way to solve this is import django settings like below four lines
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # replace with your project name
# django.setup()


# Second way to solve this is using management command that i have written in product/management/commands/run_consumer.py (recommended)


# # consumer.py
# from kombu import Connection, Exchange, Queue, Consumer
# from product.models import Product

# rabbit_url = "amqp://guest:guest@localhost:5672//"
# connection = Connection(rabbit_url)

# exchange = Exchange('product_creation_events', type='direct', durable=True)
# queue = Queue('product_created_queue', exchange, routing_key='prdouct.create', durable=True)

# def process_product_create_request(body, message):
#     print(f"Processing product: {body['product_name']}")
#     # TODO: Do further processing (DB update, email, etc.)
#     print("body", body)
#     print("message", message)
#     Product.objects.create(name=body['product_name'])
#     print(f"Product {body['product_name']} created successfully.")
#     message.ack()

# with connection:
#     with Consumer(connection, queues=queue, callbacks=[process_product_create_request], accept=['json']):
#         print("Waiting for messages. Press Ctrl+C to exit.")
#         while True:
#             connection.drain_events()
