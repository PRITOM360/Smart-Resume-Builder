from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ResumeAnalytics
from .serializers import ResumeAnalyticsSerializer

class ResumeAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = ResumeAnalytics.objects.all()
    serializer_class = ResumeAnalyticsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)