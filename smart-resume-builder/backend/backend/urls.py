from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/resumes/', include('apps.resumes.urls')),
    path('api/ai/', include('apps.ai.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
]