from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import YourModelViewSet

router = DefaultRouter()
router.register(r'yourmodels', YourModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
