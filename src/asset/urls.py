from django.urls import path

from .views import AssetListView
from . import views

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('<int:asset_id>/', views.asset_detail),
]
