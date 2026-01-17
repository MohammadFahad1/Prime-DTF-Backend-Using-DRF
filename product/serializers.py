from rest_framework import serializers
from product.models import ReadyToPress, CustomDesign, CustomDesignPhoto

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