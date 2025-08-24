from django.db import models
from django.contrib.auth.models import User

class ShortenedURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortened_urls')
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

