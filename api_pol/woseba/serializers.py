from rest_framework.serializers import ModelSerializer

from woseba.models import Kawa


class KawaSerializer(ModelSerializer):

    class Meta:
        model = Kawa
        fields = ('nazwa', 'cena', 'ilosc')