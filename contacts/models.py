from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=200)
    vehicle = models.CharField(max_length=5, default="")
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    message = models.TextField(blank=True)
    listing_email = models.EmailField(default="")
    def __str__(self):
        return self.name
