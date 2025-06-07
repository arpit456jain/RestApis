from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # This includes all fields of the Task model
    # def create(self, validated_data):
    #     return TaskSerializer().create(**validated_data)   