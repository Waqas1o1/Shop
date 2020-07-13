from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Order
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
        
        messages.add_message(request,messages.SUCCESS,'Order i placsed succesfuly')
    return HttpResponse('Ok')
