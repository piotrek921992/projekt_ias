from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response

from hub.settings import API_POL_URL, API_ENG_URL


MAPPING = {'nazwa': 'name',
           'cena': 'price',
           'ilosc': 'stock'}
CURRENCY = 'currency'

@api_view(['GET'])
def integration_view(request):
    response_pol = requests.get(API_POL_URL).json()
    response_eng = requests.get(API_ENG_URL).json()

    normalized_pol = [
        {MAPPING[k]: v for k, v in d.items()} for d in response_pol]

    normalized_pol = [{CURRENCY: 'PLN', **d} for d in normalized_pol]
    normalized_eng = [{CURRENCY: 'USD', **d} for d in response_eng]
    return Response(normalized_pol + normalized_eng)


