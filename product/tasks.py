# from celery import shared_task
# from product.models import Product
# import time
# from myproject.celery import app
# from django_celery_results.models import TaskResult

# @shared_task
# def create_product(product_no, delay):
#     time.sleep(delay)
#     Product.objects.create(name="Product_" + str(product_no), is_active=True)


# @app.task(queue='high_priority')
# def create_product_high(product_no):
#     time.sleep(3)
#     Product.objects.create(name="Product_" + str(product_no), is_active=True)


# @app.task(queue='low_priority')
# def create_product_low(product_no):
#     time.sleep(5)
#     Product.objects.create(name="Product_" + str(product_no), is_active=True)


# @shared_task
# def reprocess_failed_tasks():
#     failed_tasks = TaskResult.objects.filter(status="FAILURE")
#     for task in failed_tasks:
#         # Decide what to do – maybe reapply task with same args
#         original_task = task.task_name
#         args = task.task_args
#         kwargs = task.task_kwargs

#         # You can retry only certain tasks
#         if original_task == "myapp.tasks.process_order":
#             from myapp.tasks import process_order
#             process_order.apply_async(args=args, kwargs=kwargs)

#         # Optional: mark old record so we don’t retry infinitely
#         task.delete()


# @app.task(queue='production_creation_dead_letter_queue')
# def create_product_dead_letter_queue(product_no):
#     # Raising an exception to simulate a failure. so that it goes to dead letter queue
#     a = 2 / 0
#     Product.objects.create(name="Product_" + str(product_no), is_active=True)
