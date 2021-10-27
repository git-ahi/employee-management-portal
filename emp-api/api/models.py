from django.db import models
from datetime import date

# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=70)
    Department = models.CharField(max_length=70)
    DateOfJoining = models.DateField(default= date.today)
    PhotoFileName = models.CharField(max_length=100)
