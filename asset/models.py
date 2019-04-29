from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Asset(models.Model):
    STATE = (
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('SA', 'South Australia'),
        ('WA', 'Western Australia'),
        ('NT', 'Northern Territory'),
        ('TAS', 'Tasmania'),
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=3, choices=STATE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset_multiple_detail', kwargs={'pk': self.pk})
