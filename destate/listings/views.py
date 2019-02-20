from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
# Create your views here.

def index(req):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 3)
    # 
    page = req.GET.get("page")
    # 
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }
    print(listings)
    return render(req, "listings/listings.html", context)

def listing(req, listing_id):
    return render(req, "listings/listing.html")

def search(req):
    return render(req, "listings/search.html")