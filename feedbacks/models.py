from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(default="")
    message = models.TextField(blank=True)
    def __str__(self):
        return self.name
