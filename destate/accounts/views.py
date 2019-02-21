from django.shortcuts import render

# Create your views here.
def register(req):
    return render(req, "accounts/register.html")

def login(req):
    return render(req, "accounts/login.html")

def logout(req):
    return redirect(req, "index")

def dashboard(req):
    return render(req, "accounts/dashboard.html")