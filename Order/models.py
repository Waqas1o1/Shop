from django.db import models
from Home.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Order_Detail(models.Model):
    Full_Name = models.CharField(max_length=50)
    Country = models.CharField(max_length=30)
    Street_Adress = models.CharField(max_length=2000)
    Post_Code = models.IntegerField()
    City_or_Town = models.CharField(max_length=30)
    Email = models.EmailField(primary_key=True)
    Phone = models.IntegerField(verbose_name="Contact Number")
    def __str__(self):
        return self.Email 
class Order(models.Model):
    Order = models.TextField(max_length=50000)
    Billing = models.ForeignKey(Order_Detail,on_delete=models.CASCADE)  
    def __str__(self):
        return self.Billing.Email
      

    

