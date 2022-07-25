
from django.db import models

# Create your models here.
class Customer(models.Model):
    customerId = models.AutoField(auto_created=True,primary_key=True)
    customerName = models.CharField(max_length=25)
    customerPhone = models.CharField(max_length=10)
    customerAddress = models.TextField(max_length=100)
    customerEmail = models.EmailField(max_length=50)
    customerPasw =models.CharField(max_length=20)


    class Meta:
        db_table = "Customer"

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(customerEmail = email)
        except:
            return False
            
