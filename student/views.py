from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializers, MarkSerializers
from .models import Student, markList
# Create your views here.
class StudentListView(ListAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()

class MarkListView(ListAPIView):
    serializer_class = MarkSerializers
    queryset = markList.objects.all()

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()

class MarkDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MarkSerializers
    queryset = markList.objects.all()