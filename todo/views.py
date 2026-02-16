from django.shortcuts import render, redirect
from .models import Account

# Create your views here.
def homePageView(request):
    return render(request, "index.html")

def registerPageView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            account = Account(username=username, password=password1)
            account.save()
            return redirect("index")
    return render(request, "register.html")

def loginPageView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        exists = Account.objects.filter(username=username, password=password)
        if exists:
            return render(request, "index.html", {"signed_in":True, "username":username})
    return render(request, "login.html")

