from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from confluent_kafka import Producer

# Kafka Producer Configuration
producer_config = {'bootstrap.servers': '172.23.224.190:9092'}
producer = Producer(producer_config)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        response = requests.get(f"http://172.23.224.190:8001/api/products/{product_id}")
        if response.status_code == 200:
            product_data = response.json()
            if product_data["stock"] >= quantity:
                order = Order.objects.create(product_id=product_id, quantity=quantity)

                # Publish message to Kafka
                producer.produce('my-topic', key=str(order.id), value=f"New order placed: {order.id}")
                producer.flush()

                return Response({"message": "Order placed successfully", "order_id": order.id})
            return Response({"error": "Not enough stock"}, status=400)
        return Response({"error": "Product not found"}, status=404)

