from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item3
from .models import Item1
from .models import Academic
from .models import Financial

class Item3Serializer(serializers.ModelSerializer):
    class Meta:

        model= Item3
        fields= '__all__'


class Item1Serializer(serializers.ModelSerializer):
    class Meta:

        model= Item1
        fields= '__all__'


class AcademicSerializer(serializers.ModelSerializer):
    class Meta:

        model= Academic
        fields= '__all__'
        

 

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:

        model= Financial
        fields= '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user