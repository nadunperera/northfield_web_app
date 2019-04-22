from django.db import models

# Create your models here.
class Asset(models.Model):
    name = models.TextField()
    address = models.TextField()
    suburb = models.TextField()
    postcode = models.TextField()
    state = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)