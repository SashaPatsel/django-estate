from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
# Create your views here.

def index(req):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(req, "listings/listing.html", context)

def search(req):
    return render(req, "listings/search.html")