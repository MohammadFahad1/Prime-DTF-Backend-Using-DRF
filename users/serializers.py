from rest_framework import serializers
from users.models import Messages
from django.contrib.auth import get_user_model
from users.models import TopHeader1, TopHeader2, HeroSectionButton

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'bio', 'address', 'phone', 'image')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'message']
        extra_kwargs = {'name': {'required': True},
                        'email': {'required': True},
                        'subject': {'required': True},
                        'message': {'required': True}} 

class TopHeader1Serializer(serializers.ModelSerializer):    
    class Meta:
        model = TopHeader1
        fields = ['id', 'message']

class TopHeader2Serializer(serializers.ModelSerializer):    
    class Meta:
        model = TopHeader2
        fields = ['id', 'message']

class HeroSectionButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionButton
        fields = ['id', 'button_text', 'button_link']
        extra_kwargs = {'button_text': {'required': True},
                        'button_link': {'required': True}}