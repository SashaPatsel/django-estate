from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(req):
    if req.method == "POST":
        #Register new user
        messages.error(req, "Testing error message")
        return redirect("register")
    else:
        return render(req, "accounts/register.html")

def login(req):
    if req.method == "POST":
        #Register new user
        return
    else:
        return render(req, "accounts/login.html")

def logout(req):
    return redirect(req, "index")

def dashboard(req):
    return render(req, "accounts/dashboard.html")