from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
from realtors.models import Realtor


# Create your views here.
def index(req):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3] #[:3] means we only want three listings
    context = {
        "listings": listings,
        "state_choices": state_choices,
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices
    }

    return render(req, "pages/index.html", context)

def about(req):
    #get all realtors
    realtors = Realtor.objects.order_by("-hire_date")

    #get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }
    return render(req, "pages/about.html", context)
    