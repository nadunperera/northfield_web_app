from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Asset


# Create your views here.
class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    context_object_name = 'assets'
    ordering = ['-created']


class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    context_object_name = 'asset'


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    fields = ['name', 'address', 'suburb', 'postcode', 'state']


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    fields = ['name', 'address', 'suburb', 'postcode', 'state']
