from django.shortcuts import render

# Create your views here.

def index(req):
    render(req, "listings/listings.html")

def listing(req):
    render(req, "listings/listing.html")

def search(req):
    render(req, "listings/search.html")