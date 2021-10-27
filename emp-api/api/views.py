from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import Departments,Employees
from api.serializers import DepartmentSerializer,EmployeeSerializer
from django.core.files.storage import default_storage

# Create your views here.
@api_view(['GET', 'POST' , 'PUT','DELETE'])


def departmentsApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return Response(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_serializer = DepartmentSerializer(data=request.department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response("Added Successfully!!" , safe=False)
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
       
    elif request.method=='PUT':
        department=Departments.objects.get(DepartmentId=request.department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=request.department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response("Updated Successfully!!", safe=False)
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST' , 'PUT','DELETE'])

def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return Response(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_serializer = EmployeeSerializer(data=request.employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
     
    elif request.method=='PUT':
        employee=Employees.objects.get(EmployeeId=request.employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=request.employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response("Updated Successfully!!", safe=False)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['SAVE'])
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return Response(file_name,safe=False)