from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'consultancy/index.html')

def contact(request):
    print(request.POST)
    return redirect("home")