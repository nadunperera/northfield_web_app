from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Asset


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


class AssetDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Asset
    context_object_name = 'asset'

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.owner:
            return True
        return False


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
