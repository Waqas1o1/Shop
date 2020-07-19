from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Order,Order_Detail
import json
# Create your views here.
def Placse_order(request):
    if request.method == 'POST':
        first_neme = request.POST['firstname']
        last_neme = request.POST['lastname']
        country = request.POST['country']
        street = request.POST['street']
        street2 = request.POST['street2']
        postcode = request.POST['zipcode']
        City_or_town = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        order = request.POST['order']
        billing = Order_Detail(Full_Name=first_neme+' '+last_neme,Country=country,Street_Adress=street + ' // ' + street2
                    ,Post_Code=int(postcode),City_or_Town=City_or_town,Email=email,Phone=phone)
        billing_obj = billing.save()
        order_dict = json.loads(order)
        porduct_list = []
        for pdc_list in order_dict.values():
            porduct_list.append({'Name':pdc_list[1],'Quantity':pdc_list[0],
                                      'Actual_Pricse':pdc_list[2],'size':pdc_list[4],
                                      })
        send_order = Order(Order=porduct_list,Billing=billing)
        send_order.save()
        messages.add_message(request,messages.SUCCESS,'Order is placsed succesfuly')
    return redirect('HomePage')
