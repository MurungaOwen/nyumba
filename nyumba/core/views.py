from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Houses
import json
# Create your views here.
def home(request):
    data=Houses.objects.all().values()
    return JsonResponse({"houses":list(data)})#display data from the database as a dict

def index(request):
    data=Houses.objects.all().values()
    data=list(data)
    return render(request,"core/index.html")