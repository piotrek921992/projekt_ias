from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from jacobs.models import Coffee
from jacobs.serializers import CoffeeSerializer


class CoffeeViewSet(viewsets.ModelViewSet):

    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    permission_classes = [AllowAny]
