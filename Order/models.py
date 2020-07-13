from django.db import models
from Home.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    order = models.CharField(max_length=100000)
    def __str__(self):
        return self.name

