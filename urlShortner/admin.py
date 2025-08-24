from django.contrib import admin
from .models import ShortenedURL



@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'user', 'created_at')
    search_fields = ('short_code', 'original_url', 'user__username')
    list_filter = ('created_at',)
