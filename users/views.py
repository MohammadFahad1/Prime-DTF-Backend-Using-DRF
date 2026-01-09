from django.shortcuts import render
from rest_framework import generics
from .serializers import MessageSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import TopHeader1, TopHeader2, HeroSectionButton
from users.serializers import TopHeader1Serializer, TopHeader2Serializer, HeroSectionButtonSerializer

# Create your views here.
class CreateMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer

class TopHeader1ViewSet(ModelViewSet):
    queryset = TopHeader1.objects.all()
    serializer_class = TopHeader1Serializer

class TopHeader2ViewSet(ModelViewSet):
    queryset = TopHeader2.objects.all()
    serializer_class = TopHeader2Serializer

class HeroSectionButtonViewSet(ModelViewSet):
    queryset = HeroSectionButton.objects.all()
    serializer_class = HeroSectionButtonSerializer