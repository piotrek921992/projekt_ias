from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from woseba.models import Kawa
from woseba.serializers import KawaSerializer


class KawaViewSet(viewsets.ModelViewSet):

    queryset = Kawa.objects.all()
    serializer_class = KawaSerializer
    permission_classes = [AllowAny]