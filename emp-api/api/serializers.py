from rest_framework import serializers
from api.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['DepartmentId', 'DepartmentName']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['EmployeeId', 'EmployeeName',
                  'Department', 'DateOfJoining', 'PhotoFileName']
