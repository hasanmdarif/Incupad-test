from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class markList(models.Model):
    studentId = models.CharField(max_length=10, validators=[alphanumeric], null=False)
    studentName = models.CharField(max_length=100, null=False)
    courseName =  models.CharField(max_length=100, null=False)
    marks = models.CharField(max_length=100, null=False)
    year = models.CharField(max_length=100, null=False)

class Student(models.Model):
    studentId = models.CharField(max_length=10, validators=[alphanumeric], null=False, unique=True)
    fullName = models.CharField(max_length=100, null=False,)
    email = models.EmailField(max_length=100, null=False,)
    address = models.CharField(max_length=100, null=False,)
    guardianName = models.CharField(max_length=100, null=False,)



