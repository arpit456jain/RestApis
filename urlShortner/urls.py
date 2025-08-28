from django.urls import path
from .views import ShortenURLView,GetOriginalURLView,RedirectShortURLView

urlpatterns = [
    path('shorten', ShortenURLView.as_view(), name='shorten-url'),
    path('originalUrl', GetOriginalURLView.as_view(), name='get-original-url'),
    path('<str:short_code>', RedirectShortURLView.as_view(), name='redirect_short_url'),
]
