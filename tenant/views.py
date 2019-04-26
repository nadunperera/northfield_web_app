from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tenant
from .forms import TenantCreateForm


# Create your views here.
class TenantListView(LoginRequiredMixin, ListView):
    model = Tenant
    context_object_name = 'tenants'
    ordering = ['-created']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(TenantListView, self).get_queryset()
        queryset = queryset.filter(asset__owner=self.request.user)
        return queryset


class TenantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Tenant
    context_object_name = 'tenant'

    def test_func(self):
        tenant = self.get_object()
        if self.request.user == tenant.asset.owner:
            return True
        return False


class TenantCreateView(LoginRequiredMixin, CreateView):
    model = Tenant
    form_class = TenantCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class TenantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tenant
    fields = ['first_name', 'last_name', 'mobile', 'email']

    def test_func(self):
        tenant = self.get_object()
        if self.request.user == tenant.asset.owner:
            return True
        return False


class TenantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tenant
    context_object_name = 'tenant'
    success_url = '/'

    def test_func(self):
        tenant = self.get_object()
        if self.request.user == tenant.asset.owner:
            return True
        return False
