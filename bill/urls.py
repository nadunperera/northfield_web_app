from django.urls import path

from .views import BillUpdateView, BillServiceCreateView

urlpatterns = [
    # path('', BillListView.as_view(), name='bill_list'),
    # path('<int:pk>/', BillDetailView.as_view(), name='bill_detail'),
    # path('new/', BillCreateView.as_view(), name='bill_create'),
    path('new/service/<int:pk>', BillServiceCreateView.as_view(), name='bill_service_create'),
    path('<int:pk>/update/', BillUpdateView.as_view(), name='bill_update'),
    # path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
]
