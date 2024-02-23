from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, PlatoSerializer
from rest_framework.response import Response
from rest_framework.request import Request

# Aqui es donde vamos a crear toda la logica de la aplicacion


class CategoriaApiView(ListCreateAPIView):
    # Esta es la manera sencilla donde no necesitamos mucha logica
    queryset = CategoriaModel.objects.all()  # Trae info
    serializer_class = CategoriaSerializer  # Convierte la info


class PlatoApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    # Al estar esto definido esto sobrescribe en la respuesta de mi
    # servidor 🎀😁
    def get(self, request: Request):

        res = PlatoModel.objects.filter(disponibilidad=True)
        print(f'Valor enviado =>   {res}')
        return Response(data={
            'message': 'nice'
        }, status=201)
