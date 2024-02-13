from django.shortcuts import render
# from django.http import HttpResponse
from .models import Customer,Product,Order,OrderItem
from .serializers import CustomerSerializer,ProductSerializer,OrderSerializer,OrderItemSerializer
from rest_framework import generics
# Create your views here.

# def home(request):
#     return HttpResponse("<h1> This is home page <h1/>")

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer    


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer        