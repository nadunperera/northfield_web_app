from django.urls import path

from . import views

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('<int:asset_id>/', views.asset_detail),
]
