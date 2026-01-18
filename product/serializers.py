from rest_framework import serializers
from product.models import ReadyToPress, CustomDesign, CustomDesignPhoto, ProductType, Product, ProductColor, ProductImage

class ReadyToPressSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ReadyToPress
        fields = ['id', 'title', 'description', 'image', 'smprice', 'mdprice', 'lgprice', 'xlprice', 'xxlprice', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CustomDesignPhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)
    class Meta:
        model = CustomDesignPhoto
        fields = ['id', 'photo']
class CustomDesignSerializer(serializers.ModelSerializer):
    photos = CustomDesignPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = CustomDesign
        fields = ['id', 'title', 'price', 'photos']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductColorSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = ProductColor
        fields = ['id', 'color_name', 'color_code_hex', 'images']

class ProductSerializer(serializers.ModelSerializer):
    colors = ProductColorSerializer(many=True, read_only=True)
    product_type = ProductTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_type', 'title', 'smprice', 'mdprice', 'lgprice', 'xlprice', 'xxlprice', 'xxxlprice', 'colors', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']