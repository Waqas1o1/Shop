from django.db import models
from Home.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Order_details(models.Model):
    products_name = models.CharField(max_length=300) 
    products_actual_pricse = models.CharField(max_length=300)
    products_discount = models.IntegerField() 
class Order(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    order = models.ForeignKey(Order_details,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

