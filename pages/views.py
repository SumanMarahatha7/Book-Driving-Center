from django.shortcuts import render
from listings.choices import price_bike_choices, price_car_choices
from listings.models import Listing




def index(request):
    listings = Listing.objects.all()[:5]    # only 5 items shown currently in featured page.

    context = {
        'listings': listings,
        'price_bike_choices': price_bike_choices,
        'price_car_choices': price_car_choices
    }
    return render(request,'pages/index.html',context)


def aboutus(request):
    return render(request,'pages/aboutus.html')


