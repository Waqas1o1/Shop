from django.db import models
from datetime import datetime as dt
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from datetime import datetime as dt 
from django_resized import ResizedImageField
# Create your models here.
# ######## Products
class Tag(models.Model):
    tag = models.CharField(max_length=30)
    pub_date = models.DateField()
    def __str__(self):
        return self.tag
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True) 
    product_category = models.CharField(max_length=30)
    product_publishDate = models.DateTimeField(default='',)
    product_cover = ResizedImageField(size=[470,620],quality=100,blank=True)
    product_baneer = models.ImageField()
    
    def __str__(self):
        return self.product_category 
    
class Coupen(models.Model):
    code = models.CharField(max_length=30)
    issue_date = models.DateTimeField(default=dt.now)
    expire_date = models.DateTimeField()
    discount = models.IntegerField(help_text='In Percsent')
    def __str__(self):
        return self.code
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_category = models.ForeignKey(Product,on_delete=models.CASCADE)
    item_subCategory = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30,default='') 
    item_titile = models.CharField(max_length=30) 
    item_FrashPricse = models.FloatField(max_length=30)
    item_Discount_pricse = models.FloatField(max_length=30,default=0.00)
    item_discription = models.TextField()
    item_image = ResizedImageField(size=[270,330],quality=100)
    item_quantity = models.IntegerField()
    item_weight = models.FloatField(default=1.0,help_text="In KG")
    item_publishDate = models.DateTimeField() 
    #sizes 
    small = models.BooleanField(default=False)
    extra_samll = models.BooleanField(default=False)
    medium = models.BooleanField(default=True)
    large = models.BooleanField(default=False)
    extra_large = models.BooleanField(default=False)
    # Colro's Choise 
    item_color1 = ColorField(default='#FF0000')
    item_color2 = ColorField(null=True)
    item_color3 = ColorField(null=True)
    # Extra images of item
    item_zoom_pic1 = ResizedImageField(size=[440,520],keep_meta=True,quality=100,blank=True)
    item_zoom_pic2 = ResizedImageField(size=[440,520],quality=100,blank=True)
    item_zoom_pic3 = ResizedImageField(size=[440,520],quality=100,blank=True)
    # Cuppen
    item_coupen = models.ManyToManyField(Coupen)
    # tags
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.item_name + ' ' + self.item_titile

class Promotions(models.Model):
    promoion_id = models.AutoField(primary_key=True)
    promotion_title = models.CharField(max_length=100)
    promotion_name = models.CharField(max_length=100)
    promotion_desc = models.TextField()
    promotion_up_to = models.IntegerField()
    promotion_catagory = models.ForeignKey(Product,on_delete=models.CASCADE)
    promotion_item = models.ForeignKey(Item,models.CASCADE)
    promtion_cover1 = ResizedImageField(size=[1920,728],quality=100,blank=True)
    promotion_duration = models.DateTimeField(default=dt.now)
    def __str__(self):
        return self.promotion_name + ' ' + self.promotion_title
class TimeDeal(models.Model):
    deal_name = models.CharField('Name Of the Deal',max_length=50,help_text='This will display so it must be correct')
    deal_desc = models.TextField()
    deal_catg = models.ForeignKey(Product,on_delete=models.CASCADE)
    deat_duration = models.TimeField('Duration Time')
    deal_img = models.ImageField('Deal Of The Day Cover Image')
    def __str__(self):
        return self.deal_name


class ItemComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Item, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=dt.now)
    def __str__(self):
        return self.comment[:20] + ' : ' + str(self.user)