from django.shortcuts import render, redirect
from .models import Account

# Create your views here.
def homePageView(request):
    return render(request, "index.html")

def registerPageView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        account = Account(username=username, password=password)
        account.save()
        return redirect("index")
    return render(request, "register.html")

def loginPageView(request):
    if request.method == "POST":
        pass # Add login functionality later!!!
    return render(request, "login.html")

