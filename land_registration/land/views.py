from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import json
import math
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

def optimization(bid_land_obj, account_address):
    objects = bid_land_obj.bidlands.filter(itter = bid_land_obj.itter -1)
    owner_obj = objects.get(buyer = False)
    buyer_obj = objects.filter(buyer = True)
    return_text ="Error"
    result = []
    for obj in buyer_obj:
        value_diff = owner_obj.value - obj.value
        # make the value diff 0 if bid is higher than then required
        if value_diff < 0:
            value_diff = 0
        days_diff = owner_obj.days - obj.days
        if days_diff > 0:
            days_diff = 0
        token_money_diff = owner_obj.token_money - obj.token_money
        if token_money_diff > 0:
            token_money_diff = 0
        result.append((obj.account, math.sqrt((value_diff)**2)))
    result.sort(key = lambda x : x[1])
    print(result)
    if result[0][0]!=account_address:
        return_text = "You should increase your bid."
    else:
        return_text = "You can decrease your bid."
    return return_text

@login_required(login_url='/user/login')
def bidding(request,pk):
    context ={
        "land_number": pk,
        "bidder_address": request.user.account_address,
    }
    land_obj = Land.objects.filter(land_id = pk)
    if land_obj.exists():
        land_obj = land_obj.first()
        bid_land_obj = land_obj.lands.all()[0] # have to fetch the latest bid
        context['land'] = bid_land_obj
        if bid_land_obj.itter > 1:
            context['suggestion'] = optimization(bid_land_obj, request.user.account_address)
            context['previous_bid'] = bid_land_obj.bidlands.get(itter = bid_land_obj.itter -1, account = request.user.account_address)
    return render(request, 'bid.html',context)

@login_required(login_url='/user/login')
def save_bid(request):
    if request.method == 'POST':
        context ={}
        bid_land_obj = BidLand.objects.get(id = request.POST.get('id'))
#        print(bid_land_obj,request.POST.get('value'), request.POST.get('address'), request.POST.get('itter'))
        account = request.POST.get('address')
        itter =  request.POST.get('itter')
        days =  request.POST.get('days')
        token_money =  request.POST.get('token_money')
        value =  request.POST.get('value')
        bid_obj = Bid.objects.filter(account = account, itter = itter, bid_land = bid_land_obj)
        if bid_obj.exists():
            bid_obj = bid_obj.first()
            bid_obj.value = value
            bid_obj.days = days
            bid_obj.token_money = token_money
            bid_obj.save()
            context['detail'] = "Bid Updated"
        else:
            Bid.objects.create(bid_land = bid_land_obj, value = value, account = account, itter = itter, days = days, token_money = token_money)
            context['detail'] = "Bid Saved"
    return render(request, 'save_bid.html',context)

# for logged in user
@login_required(login_url='/user/login')
def lands_available_db(request):
    context = {}
    context['bid_lands'] = BidLand.objects.all()
    return render(request,'db/land_available_db.html', context)
