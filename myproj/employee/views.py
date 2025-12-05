from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import EmployeeModel
from .serializer import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#viewset
class EmployeeView(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes =[IsAuthenticated]