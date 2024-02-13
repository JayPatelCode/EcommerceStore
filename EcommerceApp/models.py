from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)    
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,null=True,blank=True)

    
