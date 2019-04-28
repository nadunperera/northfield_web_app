from django.urls import path

from .views import ServiceUpdateView, ServiceDeleteView, ServiceMultipleDetailView, ServiceAssetCreateView

urlpatterns = [
    # path('', ServiceListView.as_view(), name='service_list'),
    # path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    # path('new/', ServiceCreateView.as_view(), name='service_create'),
    path('new/asset/<int:pk>/', ServiceAssetCreateView.as_view(), name='service_asset_create'),
    path('<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    path('<int:pk>/', ServiceMultipleDetailView.as_view(), name='service_multiple_detail')
]
