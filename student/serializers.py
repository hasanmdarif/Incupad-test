from rest_framework import serializers
from .models import Student, markList
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class MarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = markList
        fields = "__all__"