from rest_framework.serializers import ModelSerializer

from ..models import Eshkhi


class ClotheSerializer(ModelSerializer):
    class Meta:
        model = Eshkhi
        fields = '__all__'
