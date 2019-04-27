from django.db import models
from tenant.models import Tenant
from django.urls import reverse


# Create your models here.
class Stay(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('stay_detail', kwargs={'pk': self.pk})
