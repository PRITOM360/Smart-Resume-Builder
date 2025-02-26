from django.urls import path
from .views import ResumeListView, ResumeDetailView, ResumeCreateView, ResumeUpdateView, ResumeDeleteView

urlpatterns = [
    path('resumes/', ResumeListView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('resumes/create/', ResumeCreateView.as_view(), name='resume-create'),
    path('resumes/update/<int:pk>/', ResumeUpdateView.as_view(), name='resume-update'),
    path('resumes/delete/<int:pk>/', ResumeDeleteView.as_view(), name='resume-delete'),
]