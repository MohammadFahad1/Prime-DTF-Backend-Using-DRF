from django.shortcuts import render
from rest_framework import generics
from .serializers import MessageSerializer

# Create your views here.
class CreateMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer