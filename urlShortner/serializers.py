from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'user', 'original_url', 'short_code', 'created_at']
        read_only_fields = ['id', 'short_code', 'created_at']