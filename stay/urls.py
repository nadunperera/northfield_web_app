from django.urls import path

from .views import StayListView, StayCreateView, StayUpdateView, StayDetailView

urlpatterns = [
    path('', StayListView.as_view(), name='stay_list'),
    path('<int:pk>/', StayDetailView.as_view(), name='stay_detail'),
    path('new/', StayCreateView.as_view(), name='stay_create'),
    path('<int:pk>/update/', StayUpdateView.as_view(), name='stay_update'),
    # path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
]
