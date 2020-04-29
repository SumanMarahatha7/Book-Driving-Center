from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'phone', 'time', 'vehicle', 'email' , 'contact_date')
    list_display_links = ('id','name')
    search_fields = ('name', 'listing', 'time', 'vehicle', 'contact_date')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

# Register your models here.
