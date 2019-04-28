from django.urls import path

from .views import StayUpdateView, StayTenantCreateView

urlpatterns = [
    # path('', StayListView.as_view(), name='stay_list'),
    # path('<int:pk>/', StayDetailView.as_view(), name='stay_detail'),
    # path('new/', StayCreateView.as_view(), name='stay_create'),
    path('new/tenant/<int:pk>', StayTenantCreateView.as_view(), name='stay_tenant_create'),
    path('<int:pk>/update/', StayUpdateView.as_view(), name='stay_update'),
    # path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
]
