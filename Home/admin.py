from django.contrib import admin
from .models import Product,Item,Promotions,TimeDeal,ItemComment,Tag
from .models import Coupen
# Register your models here.
admin.site.register((Product,Item,Promotions,TimeDeal,ItemComment,Coupen,Tag))