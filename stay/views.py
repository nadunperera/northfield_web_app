from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from .models import Stay
from .forms import StayCreateUpdateForm


# Create your views here.
# class StayListView(LoginRequiredMixin, ListView):
#     model = Stay
#     context_object_name = 'stays'
#     ordering = ['-created']
#     paginate_by = 10
#
#     def get_queryset(self):
#         queryset = super(StayListView, self).get_queryset()
#         queryset = queryset.filter(tenant__asset__owner=self.request.user)
#         return queryset


# class StayDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Stay
#     context_object_name = 'stay'
#
#     def test_func(self):
#         stay = self.get_object()
#         if self.request.user == stay.tenant.asset.owner:
#             return True
#         return False


# Not using now
# class StayCreateView(LoginRequiredMixin, CreateView):
#     model = Stay
#     form_class = StayCreateUpdateForm
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['owner'] = self.request.user
#         return kwargs


class StayTenantCreateView(LoginRequiredMixin, CreateView):
    model = Stay
    form_class = StayCreateUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        kwargs['tenant_id'] = self.kwargs['pk']
        return kwargs


class StayUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Stay
    form_class = StayCreateUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def test_func(self):
        stay = self.get_object()
        if self.request.user == stay.tenant.asset.owner:
            return True
        return False
