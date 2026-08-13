from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import Todo, Account
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homePageView(request):
    if request.method == "POST":
        if "Delete" in request.POST:
            todo_id = request.POST.get("todo_id")
            Todo.objects.filter(id=todo_id, owner=request.session.get("username")).delete()
        else:
            todo = request.POST.get("todo")
            todo = Todo(content=todo, owner=request.session.get("username"))
            # print(todo.owner)
            todo.save()
        return redirect("index")

    todos = Todo.objects.filter(owner=request.session.get("username"))

    return render(request, "index.html", {"todos":todos, "signed_in":request.session.get("signed_in"), "username":request.session.get("username")})

    # if request.method == "POST":
    #     if not request.user.is_authenticated:
    #         return redirect("login")

    #     if "Delete" in request.POST:
    #         todo_id = request.POST.get("todo_id")
    #         Todo.objects.filter(id=todo_id, owner=request.user).delete()
    #     else:
    #         content = request.POST.get("todo", "").strip()
    #         if content:
    #             Todo.objects.create(content=content, owner=request.user)
    #     return redirect("index")

    # if request.user.is_authenticated:
    #     todos = Todo.objects.filter(owner=request.user)
    # else:
    #     todos = Todo.objects.none()

    # return render(request, "index.html", {
    #     "todos":todos, 
    #     "signed_in":request.user.is_authenticated, 
    #     "username":request.user.username,
    #     })

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
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect("index")
    # else:
    #     form = UserCreationForm()
    # return render(request, "register.html", {"form": form})

def loginPageView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        exists = Account.objects.filter(username=username, password=password)
        if exists:
            # store username in session so new todos have an owner
            request.session["username"] = username
            request.session["signed_in"] = True
            return redirect("index")
    return render(request, "login.html")
    # if request.method == "POST":
    #     username = request.POST.get("username", "").strip()
    #     password = request.POST.get("password", "")
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("index")
    #     else:
    #         messages.error(request, "Invalid username or password!")
    # return render(request, "login.html")

def logoutPageView(request):
    if "signed_in" in request.session:
        request.session["signed_in"] = False
        del request.session["username"]
    return redirect("index")
    # logout(request)
    # return redirect("index")

def triggerErrorView(request):
    raise RuntimeError("Error demonstration")