from django.shortcuts import render,HttpResponse,redirect
from Blog.models import Blog_Post
from FAQ.models import FAQ
from Home.models import Item
from django.db.models import Q
# Create your views here.
def Search(request,ctg):
    search = request.GET.get('search')
    if ctg == "Shop":
        d = Item.objects.filter(Q(item_titile__icontains=search) | Q(item_name__icontains=search) | Q(item_subCategory__icontains=search) | Q(item_discription__icontains=search)) 
        send_dict = {'items':d}
        return render(request,'home/shop.html',send_dict)
    if ctg == 'Blog':
        d = Blog_Post.objects.filter(Q(title__icontains=search) | Q(catagory__icontains=search) | Q(Paragraph__icontains=search) | Q(blog_auther__icontains=search) | Q(auther_bio__icontains=search))
        send_dict = {'Posts':d}
        return render(request,'blog/blog.html',send_dict)
    if ctg == 'Faq':
        d = FAQ.objects.filter(Q(Question__icontains=search) | Q(Answer__icontains=search) | Q(Answer2__icontains=search) )
        send_dict = {'QA':d}
        return render(request,'faq/faq.html',send_dict)