from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue, Exchange


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

dlx_exchange = Exchange("dlx_exchange", type="direct")

app.conf.task_queues = (
    Queue('high_priority', routing_key='high_priority'),
    Queue('low_priority', routing_key='low_priority'),
    Queue(
        "production_creation_dead_letter_queue",
        exchange=Exchange("production_creation_dead_letter_queue", type="direct"),
        routing_key="production_creation_dead_letter_queue",
        queue_arguments={
            "x-dead-letter-exchange": "dlx_exchange",
            "x-dead-letter-routing-key": "dlq",
        },
    ),
    Queue(
        "dead_letter_queue",
        exchange=dlx_exchange,
        routing_key="dlq",
    ),
)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
