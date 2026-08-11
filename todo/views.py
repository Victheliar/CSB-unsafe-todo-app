from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homePageView(request):

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        if "Delete" in request.POST:
            todo_id = request.POST.get("todo_id")
            Todo.objects.filter(id=todo_id, owner=request.user).delete()
        else:
            content = request.POST.get("todo", "").strip()
            if content:
                Todo.objects.create(content=content, owner=request.user)
        return redirect("index")

    if request.user.is_authenticated:
        todos = Todo.objects.filter(owner=request.user)
    else:
        todos = Todo.objects.none()

    return render(request, "index.html", {
        "todos":todos, 
        "signed_in":request.user.is_authenticated, 
        "username":request.user.username,
        })

def registerPageView(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken!")
            return render(request, "register.html")
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, "register.html")
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect("index")
    return render(request, "register.html")

def loginPageView(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, "login.html")

def logoutPageView(request):
    logout(request)
    return redirect("index")