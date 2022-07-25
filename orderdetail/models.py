
from email.policy import default
from django.db import models

from customer.models import Customer
from product.models import Product

# Create your models here.

class OrderDetail(models.Model):
    orderId = models.AutoField(auto_created=True,primary_key=True)
    customerId = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    paymentStatus = models.CharField(max_length=100)
    deliverStatus =models.CharField(max_length=100)


    class Meta:
        db_table = "orderDetail"