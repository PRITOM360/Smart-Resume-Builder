from django.urls import path
from . import views

urlpatterns = [
    path('analytics/', views.AnalyticsListView.as_view(), name='analytics-list'),
    path('analytics/<int:id>/', views.AnalyticsDetailView.as_view(), name='analytics-detail'),
]