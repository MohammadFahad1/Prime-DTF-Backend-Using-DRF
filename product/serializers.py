from rest_framework import serializers
from product.models import ReadyToPress

class ReadyToPressSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ReadyToPress
        fields = ['id', 'title', 'description', 'image', 'smprice', 'mdprice', 'lgprice', 'xlprice', 'xxlprice', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']