from django.shortcuts import get_object_or_404, render
from listings.choices import price_bike_choices, price_car_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('id')

    paginator = Paginator(listings,4)                         # This is for putting only 4 list in one page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context ={
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html',context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.all()


    context = {
        'listings': Listing.objects.filter()
    }
    if 'title' in request.GET:
          title = request.GET['title']
          if title:
            listings = queryset_list.filter(description__icontains=title)

    if 'address' in request.GET:
          address = request.GET['address']
          if address:
            listings = Listing.objects.filter(address__contains=address)

            context = {
                #'price_bike_choices': price_bike_choices,
                # 'price_car_choices': price_car_choices,
                'listings': listings
                }
            return render(request, 'listings/search.html',context)


    if 'price_bike_choices' in request.GET:
          price_bike_choices = request.GET['price_bike_choices']
          if price_bike_choices:
            listings = queryset_list.filter(price_bike_choices__lte=price_bike_choices)



    context = {
    #'price_bike_choices': price_bike_choices,
    # 'price_car_choices': price_car_choices,
    'listings': listings
    }

    return render(request, 'listings/search.html',context)
