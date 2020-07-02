from django.shortcuts import render
from Home.models import Item
from Blog.models import Blog_Post
from FAQ.models import FAQ
# Create your views here.
def Search(request,ctg):
    request.GET.get(ctg)
    