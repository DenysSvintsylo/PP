from rest_framework import serializers
from main.models import Mall, City, CustomUser


class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ['id', 'address', 'description', 'city']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'city']
