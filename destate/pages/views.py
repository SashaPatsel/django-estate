from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing

# Create your views here.
def index(req):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3] #[:3] means we only want three listings
    context = {
        "listings": listings
    }

    return render(req, "pages/index.html", context)

def about(req):
    return render(req, "pages/about.html")
    