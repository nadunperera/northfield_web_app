from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Service
from bill.models import Bill
from .forms import ServiceCreateForm


# Create your views here.
# class ServiceListView(LoginRequiredMixin, ListView):
#     model = Service
#     context_object_name = 'services'
#     ordering = ['-created']
#     paginate_by = 10
#
#     def get_queryset(self):
#         queryset = super(ServiceListView, self).get_queryset()
#         queryset = queryset.filter(asset__owner=self.request.user)
#         return queryset


# Not used at the moment?
# class ServiceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Service
#     context_object_name = 'service'
#
#     def test_func(self):
#         service = self.get_object()
#         if self.request.user == service.asset.owner:
#             return True
#         return False


# Detail view for Service and Bill
class ServiceMultipleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service/service_multiple_detail.html'

    def test_func(self):
        service_multiple = self.get_object()
        if self.request.user == service_multiple.asset.owner:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(ServiceMultipleDetailView, self).get_context_data(**kwargs)
        context['bills'] = Bill.objects.filter(service=context['service'])
        return context


# Not used at the moment
# class ServiceCreateView(LoginRequiredMixin, CreateView):
#     model = Service
#     form_class = ServiceCreateForm
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['owner'] = self.request.user
#         return kwargs


class ServiceAssetCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        kwargs['asset_id'] = self.kwargs['pk']
        return kwargs


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    fields = ['name', 'category', 'provider']

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.asset.owner:
            return True
        return False


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    context_object_name = 'service'
    success_url = '/'

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.asset.owner:
            return True
        return False
