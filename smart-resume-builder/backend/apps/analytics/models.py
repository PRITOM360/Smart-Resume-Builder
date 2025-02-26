from django.db import models
from django.contrib.auth.models import User

class ResumeView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_id = models.CharField(max_length=255)
    viewed_at = models.DateTimeField(auto_now_add=True)

class ResumeDownload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_id = models.CharField(max_length=255)
    downloaded_at = models.DateTimeField(auto_now_add=True)

class ResumeAnalytics(models.Model):
    resume_id = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    last_viewed = models.DateTimeField(null=True, blank=True)

    def increment_views(self):
        self.views += 1
        self.last_viewed = models.DateTimeField(auto_now=True)
        self.save()

    def increment_downloads(self):
        self.downloads += 1
        self.save()