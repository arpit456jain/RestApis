from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskManager import views

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('task', views.getAllTask),
    path('task/<int:task_id>', views.getTaskById),
]