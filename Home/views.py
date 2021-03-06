from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Item,Promotions,TimeDeal,ItemComment,Coupen,Tag
from Blog.models import Blog_Post
from django.contrib import messages
import json
# Create your views here.
def Home(request):
    # Hole Products
    products = Product.objects.all()
    # Blogs Load
    blogs = Blog_Post.objects.all()[:3:-1]
    # Woman Products
    woman_pdt = Product.objects.filter(product_category='Woman')
    # Man Products
    Man_pdt = Product.objects.filter(product_category='Man')
    # Kid Products
    Kid_pdt = Product.objects.filter(product_category='Kid')
    ##### Woman all Items
    woman_items = Item.objects.filter(item_category=woman_pdt.first())
    #Woman Sub_Catagories 
    woman_ctg = { item.item_subCategory for item in woman_items }
    ##### Man all Items
    man_items = Item.objects.filter(item_category=Man_pdt.first())
    #Man Sub_Catagories 
    man_ctgy = { item.item_subCategory for item in man_items}
    ##### Promotion Deals
    #All Promotions
    pro = Promotions.objects.all()
    # Time Promotion
    time_pro = TimeDeal.objects.all()
    
    send_data = {'Products':products,'Promotions':pro,'Time_Deal':time_pro,"woman_items":woman_items[:20],
                'woman_ctg':woman_ctg,'man_items':man_items[:20],'man_ctg':man_ctgy,'Blogs':blogs}
    return render(request,'home/index.html',send_data)
def Product_view(request,pid):
    pdt = Item.objects.filter(item_id=pid)
    ctg = pdt[0].item_subCategory
    relative_pdt = Item.objects.all()
    search_realted = Search_pdt(relative_pdt,ctg)
    tag_id = pdt.values('tags')
    tags = []
    for tag in tag_id:
        tags.append(tag['tags'])
    p_tags = Tag.objects.filter(id = tags[0])
    #extra images
    send_ex = []
    send_ex.append(pdt[0].item_zoom_pic1)
    send_ex.append(pdt[0].item_zoom_pic2)
    send_ex.append(pdt[0].item_zoom_pic3)
    # Item Comments
    comments = ItemComment.objects.filter(post=pid)
    send_pdt = {"product":pdt[0],'realted_products':search_realted,'Tags':p_tags,'id':pid,'item_zoom_pic':send_ex,'comments':comments}
    return render(request,'home/product.html',send_pdt)

def Search_pdt(pdt,ctg):
    related = []
    for pos,p in enumerate(pdt):
        if  ctg == p.item_subCategory:
            related.append(p)
        if pos == 4:
            break
    return related

def Shop_view(request):
    items = Item.objects.all()
    tag = Tag.objects.all()
    send = {'items':items,'Tags':tag}
    return render(request,'home/shop.html',send)

def SortShop(request,shortby):
    items = Item.objects.order_by(shortby)
    send = json.dumps(product_load(items))
    return HttpResponse(send)
def Filter_products(request,filterby):
    p = Product.objects.filter(product_category=filterby).first()
    Items = Item.objects.filter(item_category=p)
    if request.is_ajax():
        data =  json.dumps(product_load(Items))
        return HttpResponse(data)
    send = {'items':Items}
    return render(request,'home/shop.html',send)
# Filter
def ByPricse(request,filter_by):
    max_amount = request.GET.get('Maxamount',None)
    min_amount = request.GET.get('Minamount',None)
    filter_item = Item.objects.filter(item_FrashPricse__lte=max_amount[1::]).filter(
                    item_FrashPricse__gte=min_amount[1::])
    data = json.dumps(product_load(filter_item))
    return HttpResponse(data)
def BySizes(request):
    size = request.GET.get('Size',None)
    if size == 'small':
        items = Item.objects.filter(small=True) 
    if size == 'xsmall':
        items = Item.objects.filter(extra_samll=True)
    if size == 'medium':
        items =Item.objects.filter(medium=True)
    if size == 'large':
        items =Item.objects.filter(large=True)
    if size == 'xlarge':
        items =Item.objects.filter(extra_large=True)
    if request.is_ajax():
        data = json.dumps(product_load(items))
        return HttpResponse(data)
    send = {'items':items}
    return render(request,'home/shop.html',send)
def ByTags(request):
    tag = request.GET.get('tag',None)
    items = Item.objects.filter(tags=tag);
    data = json.dumps(product_load(items))
    return HttpResponse(data)
# Private Funtion
def product_load(p):
    item_list = []
    for item in p:
        item_list.append({'id':item.item_id,'name':item.item_name,'title':item.item_titile,
                        'pricse':item.item_FrashPricse,'dicsount':item.item_Discount_pricse,
                        'image':str(item.item_image)})
    return item_list        
# Comments
def Comment_handle(request,pid):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        item = Item.objects.filter(item_id=pid).first()
        c = ItemComment(comment=comment,user=user,post=item)
        c.save()
        messages.add_message(request,messages.SUCCESS,'Comment is posted')

    return redirect('/product/'+str(pid))
def Search_Shop(request):
    if request.is_ajax():
        search = request.GET.get('search',None)
        data = Item.objects.filter(item_titile__icontains=search)
        send_data = json.dumps(product_load(data))
        return HttpResponse(send_data)
def ShopCart(request):
    if request.is_ajax():
        if request.method == 'POST':
            coupen = request.POST.get('coupen')
            item_coupen = Coupen.objects.filter(code=coupen)
            send_item = Item.objects.filter(item_coupen=item_coupen.first()).values('item_id')
            # print(item_coupen[0].discount)
            d = []
            for p in send_item:
                d.append({'id':p['item_id'] ,'discount':item_coupen[0].discount})
            data = json.dumps(d)
        return HttpResponse(data)
    return render(request,'home/shopping-cart.html')
def CheckOut(request):
    return render(request,'home/check-out.html');