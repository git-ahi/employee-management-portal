from django.db import models

# Create your models here.

class Depertments(models.Model):
    DepertmentId = models.AutoField(primary_key= True)
    DepertmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId= models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length= 70)  
    Depertment = models.CharField(max_length=70)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)