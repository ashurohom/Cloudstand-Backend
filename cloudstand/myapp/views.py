from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return HttpResponse("<h1>Hello Ashitosh</h1><h2>Best Of Luck</h2>")

