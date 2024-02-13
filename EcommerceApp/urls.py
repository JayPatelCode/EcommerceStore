from django.urls import path
# from .views import CustomerListCreateAPIView,ProductListCreateAPIView,OrderListCreateAPIView,OrderItemListCreateAPIView
from .views import *
urlpatterns = [
    # path("",home,name="home_page")
    path("customers/",CustomerListCreateAPIView.as_view(),name="customer-list"),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),

    path("products/",ProductListCreateAPIView.as_view(),name="product-list"),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    path("orders/",OrderListCreateAPIView.as_view(),name="order-list"),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),


    path("order-items/",OrderItemListCreateAPIView.as_view(),name="orderitem-list"),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='orderitem-detail'),


]
