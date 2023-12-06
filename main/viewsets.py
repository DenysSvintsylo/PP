from rest_framework import viewsets
from main.models import Mall, CustomUser, City
from main.serializers import CustomUserSerializer, CitySerializer, MallSerializer
from rest_framework.permissions import AllowAny

class MallViewSet(viewsets.ModelViewSet):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer
    permission_classes = [AllowAny]


class CitylViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
