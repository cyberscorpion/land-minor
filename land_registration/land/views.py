from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def register_new_land(request):
    return render(request, 'register_new_land.html')

def user_land_details(request):
    return render(request, 'user_land_details.html')

def lands_available(request):
    return render(request, 'lands_available.html')

def load_data(request):
    return render(request, 'script.html')

def add_land_available_to_sell(request,pk):
    context ={
        "land_number": pk,
    }
    return render(request, 'add_land_available_to_sell.html',context)

