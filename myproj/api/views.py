from django.shortcuts import render
from rest_framework.response import Response
from .serializer import RegisterSerializer,PersonSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .models import person
# Create your views here.
#register generics view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
     
class PersonView(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer
    