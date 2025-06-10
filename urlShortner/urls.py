from django.urls import path
from .views import SignupView, LoginView,ShortenURLView,GetOriginalURLView,redirect_short_url

urlpatterns = [
    path('register', SignupView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('shorten', ShortenURLView.as_view(), name='shorten-url'),
    path('originalUrl', GetOriginalURLView.as_view(), name='get-original-url'),
    path('<str:short_code>', redirect_short_url, name='redirect_short_url'),
]
