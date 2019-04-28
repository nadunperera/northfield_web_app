from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from .models import Bill
from .forms import BillCreateUpdateForm


# Create your views here.
# class BillListView(LoginRequiredMixin, ListView):
#     model = Bill
#     context_object_name = 'bills'
#     ordering = ['-created']
#     paginate_by = 10
#
#     def get_queryset(self):
#         queryset = super(BillListView, self).get_queryset()
#         queryset = queryset.filter(service__asset__owner=self.request.user)
#         return queryset


# class BillDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Bill
#     context_object_name = 'bill'
#
#     def test_func(self):
#         bill = self.get_object()
#         if self.request.user == bill.service.asset.owner:
#             return True
#         return False


# Not used anymore?
class BillCreateView(LoginRequiredMixin, CreateView):
    model = Bill
    form_class = BillCreateUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class BillServiceCreateView(LoginRequiredMixin, CreateView):
    model = Bill
    form_class = BillCreateUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        kwargs['service_id'] = self.kwargs['pk']
        return kwargs


class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bill
    form_class = BillCreateUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def test_func(self):
        bill = self.get_object()
        if self.request.user == bill.service.asset.owner:
            return True
        return False
