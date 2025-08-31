from django.shortcuts import render
# from common.messaging import rabbitmq_publisher
from rest_framework.views import APIView
from rest_framework.response import Response

import product
from product.utils import generate_presigned_url
from .models import Product
import time
from django.core.cache import cache
# from product.tasks import create_product, create_product_dead_letter_queue, create_product_high, create_product_low


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all().values("id", "name")
        return Response(data=product, status=200)

    def post(self, request):
        data = request.data
        product = Product.objects.create(name=data.get("name"))
        return Response(data={"id": product.id, "name": product.name}, status=201)
    

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        file_key = product.image.name  # e.g., "products/img1.jpg"
        url = generate_presigned_url(file_key, expiration=600)  # 10 min
        return Response({
            "id": product.id,
            "name": product.name,
            "image_url": url
        })


# class ProductRedisView(APIView):
#     def post(self, request):
#         product_list = cache.get("product_list")
#         if product_list:
#             return Response(data=product_list, status=200)
#         time.sleep(5)
#         products =  Product.objects.all().values("id", "name")
#         cache.set("product_list", list(products), timeout=600)
#         return Response(data=products, status=200)
    

# class ProductCeleryView(APIView):
#     def post(self, request):
#         create_product.delay(8, 10)
#         # time.sleep(2)  # Simulate some processing time
#         create_product.delay(9, 3)
#         # time.sleep(2)
#         create_product.delay(10, 1)
#         # time.sleep(2)
#         create_product.delay(11, 1)
#         return Response(data={"message": "Product creation task has been queued."}, status=202)



# class ProductMultipleCeleryView(APIView):
#     def post(self, request):
#         create_product_low.delay(1)
#         create_product_high.delay(1)
#         return Response(data={"message": "Multiple product creation tasks have been queued."}, status=202)


# class ProductProducerSingleConsumer(APIView):
#     def post(self, request):
#         product_name = "Product_producer_single_consumer"
#         # Assuming you have a producer function to send the product creation event
#         from producer.product_creation_producer import send_product_creation_event
#         send_product_creation_event(product_name)
#         return Response(data={"message": f"Product creation event for {product_name} has been sent."}, status=202)


# class ProductProducerSingleConsumerPersisitentConnection(APIView):
#     def post(self, request):
#         product_name = "Product_producer_single_consumer_persistnet_connection"
#         # Assuming you have a producer function to send the product creation event
#         from producer.product_creation_producer import send_product_creation_event
#         rabbitmq_publisher.publish_order_event(product_name)
#         return Response(data={"message": f"Product creation event for {product_name} has been sent."}, status=202)


# class ProductDeadLetterView(APIView):
#     def post(self, request):
#         create_product_dead_letter_queue.delay(11)
#         return Response(data={"message": "product creation tasks have been queued and exception sendd to dead letter queue."}, status=202)