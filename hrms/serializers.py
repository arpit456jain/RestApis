from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class MarkAttendanceSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    date = serializers.DateField()
    status = serializers.ChoiceField(choices=["PRESENT", "ABSENT"])
