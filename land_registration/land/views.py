from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import json
from .models import *
def home(request):
    return render(request, 'home.html')
def register_new_land(request):
    return render(request, 'register_new_land.html')

def user_land_details(request):
    return render(request, 'user_land_details.html')

def lands_available(request):
    return render(request, 'lands_available.html')
def dashboard_home(request):
    return render(request, 'dashboard_home.html')

def load_data(request):
    if request.method == 'POST':
        print(request.POST.get('data'))
        x = json.loads(request.POST.get('data'))
        for i in x:
            print(i[0])
#            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
        return HttpResponse("Hello")
    return render(request, 'script.html')

def add_land_available_to_sell(request,pk):
    context ={
        "land_number": pk,
    }
    return render(request, 'add_land_available_to_sell.html',context)

@login_required(login_url='/user/login')
def bidding(request,pk):
    context ={
        "land_number": pk,
        "bidder_address": request.user.account_address,
    }
    land_obj = Land.objects.filter(land_id = pk)
    if land_obj.exists():
        land_obj = land_obj.first()
        land_bid_obj = land_obj.lands.all()[0] # have to fetch the latest bid
        context['land'] = land_bid_obj
    return render(request, 'bid.html',context)

@login_required(login_url='/user/login')
def save_bid(request):
    if request.method == 'POST':
        context ={}
        bid_land_obj = BidLand.objects.get(id = request.POST.get('id'))
#        print(bid_land_obj,request.POST.get('value'), request.POST.get('address'), request.POST.get('itter'))
        Bid.objects.create(land = bid_land_obj, value =  request.POST.get('value'), account =  request.POST.get('address'), itter =  request.POST.get('itter') )
    return render(request, 'save_bid.html',context)

# for logged in user
@login_required(login_url='/user/login')
def lands_available_db(request):
    context = {}
    context['lands'] = BidLand.objects.all()
    return render(request,'db/land_available_db.html', context)
