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
#        print(request.POST.get('data'))
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


def land_details(request,pk):
    '''
    get land details from the blockchain using land id
    '''
    context ={
        "land_number": pk,
    }
    return render(request, 'user/land_details.html',context)

def optimization(bid_land_obj, account_address):
    objects = list(bid_land_obj.bidlands.filter(itter = bid_land_obj.itter -1))
    price_list = [obj.value for obj in objects]
    days_list = [obj.days for obj in objects]
    token_money_list = [obj.token_money for obj in objects]
    n_diff = 10
    min_price = min(price_list)
    max_price = max(price_list)
    min_days = min(days_list)
    max_days = max(days_list)
    min_token_money = min(token_money_list)
    max_token_money = max(token_money_list)

    for obj in objects:
        obj.n_price = (obj.value-min_price)*n_diff/(max_price-min_price)
        obj.n_days = (obj.days-min_days)*n_diff/(max_days-min_days)
        obj.n_token_money = (obj.token_money-min_token_money)*n_diff/(max_token_money-min_token_money)

        if obj.buyer == False:
            owner_obj = obj

    objects.remove(owner_obj)

    buyer_obj = objects
    return_text ="Error"
    result = []
    for obj in buyer_obj:
        value_diff = owner_obj.n_price - obj.n_price
        days_diff = owner_obj.n_days - obj.n_days
        token_money_diff = owner_obj.n_token_money - obj.n_token_money
#        print(value_diff, days_diff, token_money_diff)
        result.append((obj.account, math.sqrt((value_diff**2)+(days_diff**2)+(token_money_diff**2))))

    result.sort(key = lambda x : x[1])
    print(result)
    if result[0][0]!=account_address:
        return_text = "You should increase your bidding values."
    else:
        return_text = "You can decrease your bidding values."
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
        context['bid_land_obj'] = bid_land_obj
        if bid_land_obj.itter > 1:
            context['suggestion'] = optimization(bid_land_obj, request.user.account_address)
            context['previous_bid'] = bid_land_obj.bidlands.filter(account = request.user.account_address).order_by('-itter')[0]
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


@login_required(login_url='/user/login')
def user_lands(request):
    '''
    fetch land details from the users account address
    '''
    context = {'account_address':request.user.account_address}
    return render(request,'user/user_lands.html', context)


@login_required(login_url='/user/login')
def first_bid(request):
    if request.method == 'POST':
        context = {}

        land_id = request.POST.get('land_id')
        address = request.POST.get('account_address')
        name = request.POST.get('name')
        city = request.POST.get('city')
        area = request.POST.get('area')
        land_address = request.POST.get('address')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        land_obj = Land.objects.filter(land_id = land_id)
        if land_obj.exists():
            land_obj = land_obj.first()
            land_obj.address = address
            land_obj.name = name
            land_obj.city = city
            land_obj.area = area
            land_obj.land_address = land_address
            land_obj.save()
        else:
            land_obj = Land.objects.create(
                land_id = land_id,
                address = address,
                name = name,
                city = city,
                area = area,
                land_address = land_address,
                latitude = latitude,
                longitude = longitude
            )
        context['bidder_address'] = address
        context['land_id'] = land_id
        return render(request,'user/first_bid.html', context)

@login_required(login_url='/user/login')
def save_first_bid(request):
    if request.method == 'POST':
        context ={}
#        print("here", request.POST.get('land_id'))
        land_obj = Land.objects.get(land_id = request.POST.get('land_id'))
#        print(bid_land_obj,request.POST.get('value'), request.POST.get('address'), request.POST.get('itter'))
        bidder_address = request.POST.get('bidder_address')
#        print(bidder_address)
        days =  request.POST.get('days')
        token_money =  request.POST.get('token_money')
        value =  request.POST.get('value')

        bid_land_obj = BidLand.objects.create(
            land = land_obj,
            price = value,
            owner = bidder_address,
            active = True,
            days = days,
            token_money = token_money
        )

        bid_obj = Bid.objects.filter(account = bidder_address, bid_land = bid_land_obj)
        if bid_obj.exists():
            bid_obj = bid_obj.first()
            bid_obj.value = value
            bid_obj.days = days
            bid_obj.token_money = token_money
            bid_obj.save()
            context['detail'] = "Bid Updated"
        else:
            Bid.objects.create(bid_land = bid_land_obj,buyer = False, value = value, account = bidder_address, days = days, token_money = token_money)
            context['detail'] = "Bid Saved"
    return render(request, 'save_bid.html',context)

def my_bid(request):
    context = {}
    bid_obj = Bid.objects.filter(account = request.user.account_address)
#    bid_obj = Bid.objects.all()
#    print(bid_obj[0].account)
#    for i in bid_obj:
#        print(i.account)
#    print(request.user.account_address)
    bid_land_obj_id = bid_obj.values('bid_land').distinct()
    bid_land_obj =[]
    for i in bid_land_obj_id:
        bid_land_obj.append(BidLand.objects.get(id = i['bid_land']))
    context['bid_objects'] = bid_obj
    context['bid_land_obj'] = bid_land_obj
    return render(request, 'user/my_bid.html', context)

def all_bid_iter(request):
    bid_lands = BidLand.objects.all()
    context={
        'bid_lands':bid_lands
    }
    return render(request, 'all_bid_iter.html',context)


def increase_iter(request, pk):
    context = {}
    bid_land_obj = BidLand.objects.filter(id = pk)
    if bid_land_obj.exists():
        bid_land_obj = bid_land_obj.first()
        bid_land_obj.itter += 1
        x = bid_land_obj.itter
        bid_land_obj.save()
        context['message'] = f'Iteration increased to {x}'
    else:
        context['message'] = "Object not found"
    return render(request, "message.html", context)
