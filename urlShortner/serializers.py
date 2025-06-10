from rest_framework import serializers
from .models import URLShortenerUser,ShortenedURL
from django.contrib.auth.hashers import make_password, check_password

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortenerUser
        fields = ['name', 'email', 'username', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'user', 'original_url', 'short_code', 'created_at']
        read_only_fields = ['id', 'short_code', 'created_at']