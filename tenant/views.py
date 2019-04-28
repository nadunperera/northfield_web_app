from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Tenant
from stay.models import Stay
from .forms import TenantCreateForm


# Create your views here.
# class TenantListView(LoginRequiredMixin, ListView):
#     model = Tenant
#     context_object_name = 'tenants'
#     ordering = ['-created']
#     paginate_by = 10
#
#     def get_queryset(self):
#         queryset = super(TenantListView, self).get_queryset()
#         queryset = queryset.filter(asset__owner=self.request.user)
#         return queryset


# Not used at the moment
# class TenantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Tenant
#     context_object_name = 'tenant'
#
#     def test_func(self):
#         tenant = self.get_object()
#         if self.request.user == tenant.asset.owner:
#             return True
#         return False


# Detail view for Tenant and Stay
class TenantMultipleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Tenant
    context_object_name = 'tenant'
    template_name = 'tenant/tenant_multiple_detail.html'

    def test_func(self):
        tenant_multiple = self.get_object()
        if self.request.user == tenant_multiple.asset.owner:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(TenantMultipleDetailView, self).get_context_data(**kwargs)
        context['stays'] = Stay.objects.filter(tenant=context['tenant'])
        return context


# Not used at the moment
# class TenantCreateView(LoginRequiredMixin, CreateView):
#     model = Tenant
#     form_class = TenantCreateForm
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['owner'] = self.request.user
#         return kwargs


class TenantAssetCreateView(LoginRequiredMixin, CreateView):
    model = Tenant
    form_class = TenantCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        kwargs['asset_id'] = self.kwargs['pk']
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
