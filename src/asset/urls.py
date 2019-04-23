from django.urls import path

from . import views

urlpatterns = [
    path('', views.asset_list_view),
    path('<int:asset_id>/', views.asset_detail_page),
]
