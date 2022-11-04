from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# from simple_drf.api import serializers
# from django.http import JsonResponse

# Create your views here.

# making a Post request
class StudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# making a Get request
class GetStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# making an Update request
class UpdateStudentViews(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudentViews(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# def home(response):
#     data = {
#         "message": "This is a json response"
#     }

#     return JsonResponse(data)


