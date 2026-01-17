from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import ReadyToPress, CustomDesign, Product
from product.serializers import ReadyToPressSerializer, CustomDesignSerializer, ProductSerializer

# Create your views here.


class ReadyToPress(ListAPIView):
    queryset = ReadyToPress.objects.all()
    serializer_class = ReadyToPressSerializer

class CustomDesignViewSet(ListAPIView):
    queryset = CustomDesign.objects.all()
    serializer_class = CustomDesignSerializer

class ProductViewSet(ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related('product_type').prefetch_related('colors', 'images').filter(product_type__name=self.request.query_params.get('product_type'))