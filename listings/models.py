from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=350)
    address = models.CharField(max_length=350)
    contact_number = models.CharField(max_length=150)
    listing_email = models.EmailField(default="")
    opening_time = models.CharField(max_length=1000)
    closing_time = models.CharField(max_length=1000)
    area_in_acres = models.DecimalField(max_digits=6, decimal_places=1)
    Numbers_of_bikes = models.IntegerField()
    Numbers_of_cars = models.IntegerField()
    main_image = models.ImageField(upload_to="main_image/%Y%m%d", default="")
    image1 = models.ImageField(upload_to="image1/%Y%m%d", blank=True)
    image2 = models.ImageField(upload_to="image2/%Y%m%d", blank=True)
    image3 = models.ImageField(upload_to="image3/%Y%m%d", blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price_of_bikes_per_hour = models.IntegerField()
    price_of_cars_per_hour = models.IntegerField()
    parking_available = models.BooleanField(default=False)
    def __str__(self):
        return self.title
