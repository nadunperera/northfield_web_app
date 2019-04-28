from django.urls import path

from .views import AssetListView, AssetCreateView, AssetUpdateView, \
    AssetDeleteView, AssetMultipleDetailView

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    # path('<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
    path('new/', AssetCreateView.as_view(), name='asset_create'),
    path('<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
    path('<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),
    path('<int:pk>/', AssetMultipleDetailView.as_view(), name='asset_multiple_detail'),
]
