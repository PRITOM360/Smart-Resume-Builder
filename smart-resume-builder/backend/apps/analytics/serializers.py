from rest_framework import serializers
from .models import ResumeAnalytics

class ResumeAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeAnalytics
        fields = '__all__'