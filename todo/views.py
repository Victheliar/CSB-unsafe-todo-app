from django.shortcuts import render, redirect

# Create your views here.
def homePageView(request):
    return render(request, "index.html")

def registerPageView(request):
    return render(request, "register.html")

