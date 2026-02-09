from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #body

    return HttpResponse('<h1>welcom to django</h1>')

def home(request):
    return HttpResponse('<h3>Welcome to my blog....</h3>')