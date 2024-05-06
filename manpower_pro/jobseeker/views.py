from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'jobseeker/index.html')

def login(request):
    return render(request,'jobseeker/login.html')

def register(request):
    return render(request,'jobseeker/register.html')

def contact(request):
    return render(request,'jobseeker/contact.html')

def about(request):
    return render(request,'jobseeker/about.html')


