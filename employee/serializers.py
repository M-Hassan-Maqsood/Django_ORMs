from rest_framework import serializers

from employee.models import Employee


class EmployeeCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    department = serializers.CharField(max_length=100)
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_internal_value(self, data):
        validated = super().to_internal_value(data)

        return validated

    def to_representation(self, instance):
        data = {
            "id": instance.id,
            "name": instance.name,
            "age": instance.age,
            "department": instance.department,
            "salary": f"{instance.salary}",
        }

        return data

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Employee must be at least 18 years old.")

        return value

    def validate(self, attrs):
        if attrs["department"].lower() == "hr" and attrs["salary"] < 30000:
            raise serializers.ValidationError("HR employees must have at least 30000 salary.")

        return attrs

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)

        instance.department = validated_data.get("department", instance.department)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.save()

        return instance
