from rest_framework import serializers
from .models import CategoriaModel, PlatoModel

#Trae toda la informacion convertida en un json es como un puetne
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']
