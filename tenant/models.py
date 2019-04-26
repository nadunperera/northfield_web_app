from django.db import models
from asset.models import Asset
from django.urls import reverse


# Create your models here.
class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tenant_detail', kwargs={'pk': self.pk})
