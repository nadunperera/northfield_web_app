from django.urls import path

from .views import AssetListView, AssetDetailView, AssetCreateView, AssetUpdateView

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('asset/<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
    path('asset/new/', AssetCreateView.as_view(), name='asset_create'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
]
