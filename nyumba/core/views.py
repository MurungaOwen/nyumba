from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Houses
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.contrib import messages
import json
# Create your views here.
def index(request):
    houses=Houses.objects.all()
    return render(request,"core/index.html",locals())

def data_json(request):#this returns the data of the house in json format for ajax to work on
    houses=Houses.objects.all().values()
    return JsonResponse({"houses":list(houses)})

def register_user(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user created successfully")
        else:
            messages.error(request,"error validating form")
    form=RegisterForm()
    return render(request,"core/signup.html",locals())

def login_user(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success("user logged in successfully")
        else:
            messages.error(request,"check the username or password and try again")
    form=LoginForm()
    return render(request,"core/login.html",locals())
