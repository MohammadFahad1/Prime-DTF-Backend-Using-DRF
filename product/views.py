from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import ReadyToPress
from product.serializers import ReadyToPressSerializer

# Create your views here.


class ReadyToPress(ListAPIView):
    queryset = ReadyToPress.objects.all()
    serializer_class = ReadyToPressSerializer