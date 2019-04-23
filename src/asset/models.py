from django.db import models


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
