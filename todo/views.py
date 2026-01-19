from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return render(request, "index.html")

def registerPageView(request):
    return render(request, "register.html")