from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(req):
    if req.method == "POST":
        first_name = req.POST["first_name"]
        last_name = req.POST["last_name"]
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        password2 = req.POST["password2"]

        #check if passwords match
        if password == password2:
            return
        else:
            messages.error(req, "Passwords do not match")
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