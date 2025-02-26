from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    content = models.JSONField()  # Store sections like education, experience, skills, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ResumeTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    example_image = models.ImageField(upload_to='resume_templates/')  # Path to template image

    def __str__(self):
        return self.name

class ResumeAnalytics(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='analytics')
    views = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analytics for {self.resume.title}"