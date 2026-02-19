from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeDeleteView,
    MarkAttendanceView,
    AttendanceByEmployeeView
    
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeDeleteView.as_view()),
    path('attendance/mark/', MarkAttendanceView.as_view()),
    path('attendance/<str:employee_id>/', AttendanceByEmployeeView.as_view()),
]
