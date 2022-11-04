from dataclasses import field
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    # reg_no = serializers.CharField(max_length=255)

    class Meta:
        model = Student
        fields = "__all__"

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
 