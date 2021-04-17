from django.shortcuts import render
from rest_framework import viewsets
from api_register.models import Register
from products.serializers import RegisterSerializer


class RegisterViewset(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

