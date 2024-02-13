from rest_framework import serializers
from .models import Customer,Product,Order,OrderItem
from decimal import Decimal

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


               
         #order and order items from here      
         
# class OrderItemSerializer(serializers.ModelSerializer):
#     id=serializers.IntegerField(required=False)
#     class Meta:
#         model = OrderItem
#         fields = ['id','product', 'quantity']

# class OrderSerializer(serializers.ModelSerializer):
#     order_items = OrderItemSerializer(many=True,required=False)

#     def to_representation(self, instance):
#         data = super(OrderSerializer,self).to_representation(instance)
#         if instance:
#             order_item_queryset=OrderItem.objects.filter(order=instance)
#             data["order_items"]=OrderItemSerializer(order_item_queryset,many=True).data
#         return data    

#     class Meta:
#         model = Order
#         fields = ['id','customer', 'total_amount', 'shipping_address', 'billing_address', 'created_at','order_items']

#     def create(self, validated_data):
#         order_items_data = validated_data.pop('order_items', [])
#         order = Order.objects.create(**validated_data)

#         for item_data in order_items_data:
#             product = item_data['product']
#             quantity = item_data['quantity']

#             OrderItem.objects.create(order=order, product=product, quantity=quantity)

#         return order        
                 # to here


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance:
            order_item_queryset = OrderItem.objects.filter(order=instance)
            data["order_items"] = OrderItemSerializer(order_item_queryset, many=True).data
        return data    

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_amount', 'shipping_address', 'billing_address', 'created_at', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        total_amount = sum(item_data['product'].price * item_data['quantity'] for item_data in order_items_data)

        validated_data['total_amount'] = total_amount
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order      