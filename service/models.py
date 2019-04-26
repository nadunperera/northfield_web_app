from django.db import models
from asset.models import Asset
from django.urls import reverse


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})
