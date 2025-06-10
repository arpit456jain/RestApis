from django.db import models

class URLShortenerUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return self.username
    


class ShortenedURL(models.Model):
    user = models.ForeignKey(URLShortenerUser, on_delete=models.CASCADE, related_name='shortened_urls')
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

