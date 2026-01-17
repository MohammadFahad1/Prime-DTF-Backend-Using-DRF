from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import ReadyToPress, CustomDesign
from product.serializers import ReadyToPressSerializer, CustomDesignSerializer

# Create your views here.


class ReadyToPress(ListAPIView):
    queryset = ReadyToPress.objects.all()
    serializer_class = ReadyToPressSerializer

class CustomDesignViewSet(ListAPIView):
    queryset = CustomDesign.objects.all()
    serializer_class = CustomDesignSerializer