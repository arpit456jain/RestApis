from rest_framework import serializers
from .models import Studennt,Employee

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40)

    # if we use ModelSerilizer then we dont nned to implment this create method
    def create(self, validated_data):
        return Studennt.objects.create(**validated_data) 

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # field level validation
    # validate_FieldName
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat full")
        return value
    
    #object level valiation
    def validate(self, data):
        name = data.get("name")
        city = data.get("city ")
        if (name.lower() == 'arpit' and city!='lko'):
            raise serializers.ValidationError("city must be lko")
        return data
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # read_only_fields = ['name']
    def to_internal_value(self, data):
        # Check if this is an update and if 'name' is being modified
        if self.instance and 'name' in data:
            raise serializers.ValidationError({
                'name': 'This field cannot be updated.'
            })
        return super().to_internal_value(data)
        
