from rest_framework import serializers
from .models import CategoriaModel, PlatoModel, UsuariosModel

# Trae toda la informacion convertida en un json es como un puetne


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']
        # depth = 1


class MostrarPlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']
        depth = 1


# Recuerda que el serializador señala de como es que se tiene que devolver la data
class CategoriaPlatosSerializer(serializers.ModelSerializer):
    # Para hacer esto debimo de agregar en el modelo related_name='platos'
    infoAdicional = PlatoSerializer(many=True, source='platos')

    class Meta:
        model = CategoriaModel
        fields = '__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosModel
        fields = '__all__'
        #Indico que no quiero que se me devuelva la contraseña
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
