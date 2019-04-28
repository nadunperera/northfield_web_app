from django.urls import path

from .views import TenantUpdateView, TenantDeleteView, \
    TenantMultipleDetailView, TenantAssetCreateView

urlpatterns = [
    # path('', TenantListView.as_view(), name='tenant_list'),
    # path('<int:pk>/', TenantDetailView.as_view(), name='tenant_detail'),
    # path('new/', TenantCreateView.as_view(), name='tenant_create'),
    path('new/asset/<int:pk>/', TenantAssetCreateView.as_view(), name='tenant_asset_create'),
    path('<int:pk>/update/', TenantUpdateView.as_view(), name='tenant_update'),
    path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
    path('<int:pk>/', TenantMultipleDetailView.as_view(), name='tenant_multiple_detail'),
]
