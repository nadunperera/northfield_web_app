from django.db import models
from service.models import Service
from django.urls import reverse


# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=100)
    bill_from = models.DateField()
    bill_to = models.DateField()
    discount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    discount_end = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bill_detail', kwargs={'pk': self.pk})
