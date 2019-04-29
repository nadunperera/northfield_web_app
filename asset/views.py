from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Asset
from tenant.models import Tenant
from service.models import Service


# Create your views here.
class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    context_object_name = 'assets'
    ordering = ['-created']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(AssetListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


# Not used at the moment?
# class AssetDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Asset
#     context_object_name = 'asset'
#
#     def test_func(self):
#         asset = self.get_object()
#         if self.request.user == asset.owner:
#             return True
#         return False


# Detail view for Asset, Tenant and Service
class AssetMultipleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name = 'asset/asset_multiple_detail.html'

    def test_func(self):
        asset_multiple = self.get_object()
        if self.request.user == asset_multiple.owner:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(AssetMultipleDetailView, self).get_context_data(**kwargs)
        context['tenants'] = Tenant.objects.filter(asset=context['asset']).order_by('created')
        context['services'] = Service.objects.filter(asset=context['asset']).order_by('created')
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    fields = ['name', 'address', 'suburb', 'postcode', 'state']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AssetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Asset
    fields = ['name', 'address', 'suburb', 'postcode', 'state']

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.owner:
            return True
        return False


class AssetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Asset
    context_object_name = 'asset'
    success_url = '/'

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.owner:
            return True
        return False
