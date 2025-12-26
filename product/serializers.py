from rest_framework import serializers
from product.models import ReadyToPress

class ReadyToPressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyToPress
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']