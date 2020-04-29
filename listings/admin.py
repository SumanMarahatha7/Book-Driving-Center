from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'price_of_bikes_per_hour', 'price_of_cars_per_hour', 'opening_time', 'closing_time')
    list_display_links = ('id','title')
    list_filter = ('price_of_bikes_per_hour','price_of_cars_per_hour')
    search_fields = ('title','description','address','price_of_cars_per_hour','price_of_bikes_per_hour','opening_time','closing_time')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)
