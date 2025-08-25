from django.core.management.base import BaseCommand
from kombu import Connection, Exchange, Queue, Consumer
from product.models import Product


class Command(BaseCommand):
    help = "Runs the RabbitMQ consumer for product creation events"

    def handle(self, *args, **options):
        rabbit_url = "amqp://guest:guest@localhost:5672//"
        connection = Connection(rabbit_url)

        exchange = Exchange('product_creation_events', type='direct', durable=True)
        queue = Queue(
            'product_created_queue',
            exchange,
            routing_key='prdouct.create',   # careful, looks like typo
            durable=True
        )

        def process_product_create_request(body, message):
            self.stdout.write(f"Processing product: {body['product_name']}")
            Product.objects.create(name=body['product_name'])
            self.stdout.write(self.style.SUCCESS(f"Product {body['product_name']} created successfully."))
            message.ack()

        with connection:
            with Consumer(connection, queues=queue, callbacks=[process_product_create_request], accept=['json']):
                self.stdout.write(self.style.NOTICE("Waiting for messages. Press Ctrl+C to exit."))
                while True:
                    connection.drain_events()

# This command can be run using `python manage.py product_consumer`