from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            serializer = EmployeeSerializer(
                employees, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Company not found'})

    # def create(self, request, *args, **kwargs):
    #     # Implement custom create logic here
    #     # ...
    #     print("create")
    #     return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     # Implement custom update logic here
    #     # ...
    #     print("update")
    #     return super().update(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     # Implement custom partial update logic here
    #     # ...
    #     print("partial_update")
    #     return super().partial_update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     # Implement custom delete logic here
    #     # ...
    #     print("destroy")
    #     return super().destroy(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     # Implement custom retrieve logic here
    #     # ...
    #     print("retrieve")
    #     return super().retrieve(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     # Implement custom list logic here
    #     # ...
    #     print("list")
    #     return super().list(request, *args, **kwargs)


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
