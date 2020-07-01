from django.shortcuts import render,HttpResponse
from .models import Blog_Post,BlogComment
import json
# Create your views here.
def Index(request):
    if request.is_ajax():
        ctg = request.GET.get('catagory',None)
        blog_Post = Blog_Post.objects.filter(catagory=ctg)
        send_post = json.dumps(product_send(blog_Post))
        return HttpResponse(send_post)    
    catagories = Blog_Post.objects.values('catagory')
    post = Blog_Post.objects.all()
    recent_post = Blog_Post.objects.all().order_by('publish_date')[0:4]
    ctg_set = set()
    for ctg in catagories:
        ctg_set.add(ctg['catagory'])
    return render(request,'blog/blog.html',{'Posts':post, 'Recent_posts':recent_post,'catagory':ctg_set})
def Search(request):
    if request.is_ajax():
        search = request.GET.get('search',None)
        data = Blog_Post.objects.filter(title__icontains=search)
        send_data = json.dumps(product_send(data))
        return HttpResponse(send_data)
def product_send(obj):
    item_list = []
    for i in obj:
        item_list.append({'title':i.title,'catagory':i.catagory,'Paragraph':i.Paragraph,'publish_date':str(i.publish_date.date()),'cover_img':str(i.cover_img)})
    return item_list
def BlogPost(request,bid):
    p = Blog_Post.objects.filter(id=bid)
    
    try:
        p_n = Blog_Post.objects.filter(id__gte=bid).order_by('id')[1:2]
        next_p = p_n[0]
    except:
        next_p = p_n
    try:
        p_p = Blog_Post.objects.filter(id__lte=bid).order_by('id')[::-1][1:2]
        previous = p_p[0]
    except:     
        previous = p_p
    comment = BlogComment.objects.filter(post=p.first())[:10:-1]
    return render(request,'blog/blog-details.html',{'Post':p[0],'Next_Post':next_p,'Previous_Post':previous,'comments':comment})
def Blogcomment(request,bid):
    if request.is_ajax():
        comment = request.GET.get("comment",'')
        post = Blog_Post.objects.filter(id=bid).first()
        c = BlogComment(comment=comment,user=request.user,post=post)
        c.save()
        comments = BlogComment.objects.filter(post=post)
        send = json.dumps(product_load(comments))
        return HttpResponse(send)
def product_load(obj):
    item_list = []
    for comment in obj:
        item_list.append({'Username':str(comment.user),'comment':comment.comment,'timestamp':str(comment.timestamp.date())})
    return item_list