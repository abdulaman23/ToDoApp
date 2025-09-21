from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

# Create your views here.
