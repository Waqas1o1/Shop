from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from datetime import datetime as dt
from django_resized import ResizedImageField
# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=30)
    pub_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.tag
    
class Blog_Post(models.Model):
    title = models.CharField(max_length=400)
    catagory = models.CharField(max_length=50) 
    Paragraph = HTMLField()
    blog_auther = models.CharField(max_length=300,default='')
    auther_bio = models.CharField(max_length=300,default='')
    auther_thumbnail = ResizedImageField(size=[91,89],quality=100)
    cover_img  = ResizedImageField(size=[1030,550],quality=100)
    thumbnaiil_img  = ResizedImageField(size=[410,280],quality=100)
    img_1 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    img_2 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    img_3 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    img_4 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    img_5 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    img_6 = ResizedImageField(size=[330,250],quality=100,blank=True) 
    blog_quote_1 = models.CharField(max_length=300,blank=True)
    blog_quote_2 = models.CharField(max_length=300,blank=True)
    publish_date = models.DateTimeField(default=dt.now())
    tags = models.ManyToManyField(Tag) 
    
    def __str__(self):
        return self.title 
class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=dt.now)
    def __str__(self):
        return self.comment[:20] + ' : ' + str(self.user)