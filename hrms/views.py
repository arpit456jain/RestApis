
from rest_framework import generics, status
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, Employee
from .serializers import AttendanceSerializer
from .serializers import MarkAttendanceSerializer
from .serializers import MarkAttendanceSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceByEmployeeView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee__employee_id=employee_id).order_by('-date')



class MarkAttendanceView(APIView):

    def post(self, request):
        serializer = MarkAttendanceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        employee_id = serializer.validated_data["employee_id"]
        date = serializer.validated_data["date"]
        status_value = serializer.validated_data["status"]

        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        attendance, created = Attendance.objects.update_or_create(
            employee=employee,
            date=date,
            defaults={"status": status_value}
        )

        if created:
            return Response(
                {"message": "Attendance created successfully"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Attendance updated successfully"},
                status=status.HTTP_200_OK
            )

