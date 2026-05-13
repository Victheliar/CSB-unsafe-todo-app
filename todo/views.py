from django.shortcuts import render, redirect
from .models import Account, Todo

# Create your views here.
def homePageView(request):

    if request.method == "POST":
        if "Delete" in request.POST:
            todo_id = request.POST.get("todo_id")
            Todo.objects.filter(id=todo_id, owner=request.session.get("username")).delete()
        else:
            todo = request.POST.get("todo")
            todo = Todo(content=todo, owner=request.session.get("username"))
            print(todo.owner)
            todo.save()
        return redirect("index")

    todos = Todo.objects.filter(owner=request.session.get("username"))

    return render(request, "index.html", {"todos":todos, "signed_in":request.session.get("signed_in"), "username":request.session.get("username")})

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
            # store username in session so new todos have an owner
            request.session["username"] = username
            request.session["signed_in"] = True
            return redirect("index")
    return render(request, "login.html")

def logoutPageView(request):
    if "signed_in" in request.session:
        request.session["signed_in"] = False
        del request.session["username"]
    return redirect("index")