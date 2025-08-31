from django.urls import path

from product.views import ProductDetailView, ProductView
# from product.views import ProductDeadLetterView, ProductProducerSingleConsumer, ProductProducerSingleConsumerPersisitentConnection, ProductRedisView, ProductCeleryView, ProductMultipleCeleryView



urlpatterns = [
    path('v1/products', ProductView.as_view(), name='product-list'),
    path('v1/product/details/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    # path('v1/redis/products', ProductRedisView.as_view(), name='product-list'),
    # path('v1/celery/products', ProductCeleryView.as_view(), name='product-list'),
    # path('v1/celery/products/multiple', ProductMultipleCeleryView.as_view(), name='product-list'),
    # path('v1/celery/products/producer-single-consumer', ProductProducerSingleConsumer.as_view(), name='product-list'),
    # path('v1/celery/products/producer-single-consumer-persistent-connection', ProductProducerSingleConsumerPersisitentConnection.as_view(), name='product-list'),
    # path('v1/celery/products/dead-letter-queue', ProductDeadLetterView.as_view(), name='product-list'),
]
