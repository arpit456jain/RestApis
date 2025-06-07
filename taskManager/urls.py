from django.urls import path, include
from taskManager import views


urlpatterns = [
    path('task', views.getAllTask),
    path('task/<int:task_id>', views.getTaskById),
    path('createTask', views.createTask),
    path('updateTask', views.updateTask),
    path('deleteTask/<int:task_id>', views.deleteTask),
]