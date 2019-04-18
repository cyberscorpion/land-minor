from django.shortcuts import render
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.template.loader import render_to_string
from .forms import (
    RegisterForm,
)
User = get_user_model()

# Create your views here.
def register_user(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return redirect('/user/login')
    return render(request, "user/register.html",context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'user/login.html')

def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username,password=password) #here username can be email or phone number
    if user is not None:
        if user.is_active:
            login(request,user)
        else:
            return HttpResponse("Please activate your account.")
        return redirect('/dashboard')
    else:
        return redirect('/home')

def invalid(request):
    return render(request, 'user/invalid.html')

def logout_user(request):
    logout(request)
    return redirect('/home')
