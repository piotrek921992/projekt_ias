from rest_framework.serializers import ModelSerializer

from jacobs.models import Coffee


class CoffeeSerializer(ModelSerializer):

    class Meta:
        model = Coffee
        fields = ('name', 'price', 'stock')