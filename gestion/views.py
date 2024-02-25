from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from .models import CategoriaModel, PlatoModel, UsuariosModel
from .serializers import CategoriaSerializer, PlatoSerializer, CategoriaPlatosSerializer, MostrarPlatoSerializer, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .permisions import SoloAdministradores
# Aqui es donde vamos a crear toda la logica de la aplicacion


class CategoriaApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, SoloAdministradores]
    # Esta es la manera sencilla donde no necesitamos mucha logica
    queryset = CategoriaModel.objects.all()  # Trae info
    serializer_class = CategoriaSerializer  # Convierte la info


class PlatoApiView(ListCreateAPIView):
    def get(self, request: Request):
        res = PlatoModel.objects.filter(disponibilidad=True)
        serializer = MostrarPlatoSerializer(res, many=True)
        return Response(data={
            'message': serializer.data
        }, status=201)

    def post(self, request: Request, *args, **kwargs):
        body = request.data
        serializer = PlatoSerializer(data=body)
        try:
            if not body:
                return Response(data={
                    'message': 'No te encuentras enviando ningun parametro 💣🤦‍♂️',
                }, status=400)

            platoRepetido = PlatoModel.objects.filter(
                nombre=body.get('nombre')).first()
            if platoRepetido:
                return Response(data={
                    'message': 'El plato {} ya se encuentra creado 🤷‍♂️'.format(body.get('nombre')),
                }, status=400)

            statusSeria = serializer.is_valid()

            if statusSeria:
                serializer.save()
                return Response(data={
                    'message': 'Se creo correctamente {} 💚'.format(body.get('nombre')),
                    'data': serializer.data
                }, status=201)
            else:
                return Response(data={
                    'message': 'Lo siento pero los datos enviados no cumplen con los parametros establecidos',
                    'error': serializer.errors
                }, status=201)
        except Exception as e:
            return Response(data={
                'message': 'Ocurrió un error al crear el plato {}.'.format(body.get('nombre')),
                'error_details': str(e)
            })


# Metodo encargado de hacer el soft delete a los platos que se tiene por parte del cliente
class PlatoDestroyApiView(DestroyAPIView):
    # queryset = PlatoModel.objects.all()
    # serializer_class = PlatoSerializer
    def delete(self, request: Request, pk: int):
        platoEncontrado = PlatoModel.objects.filter(
            id=pk, disponibilidad=True).first()
        if platoEncontrado is None:
            return Response(data={'msg': 'No existe tu plato'})
        platoEncontrado.disponibilidad = False
        serializer = PlatoSerializer(platoEncontrado)
        platoEncontrado.save()
        return Response(data={
            'msg': 'Se ha eliminado el plato {}'.format(platoEncontrado.nombre),
            'data': serializer.data
        })


class ListarCategoriasApiView(ListAPIView):

    def get(self, request, pk: int, **kwargs):
        categoriaEncontrada = CategoriaModel.objects.filter(id=pk).first()
        if categoriaEncontrada is None:
            return Response(data={
                'msg': 'No se pudo encontrar la  categoria asocidad al id {}'.format(pk)
            })
        serializer = CategoriaPlatosSerializer(instance=categoriaEncontrada)

        return Response(data={
            'msg': 'Se logro encontrar el mensaje correctamente',
            'data': serializer.data,
        })


class RegistrarUsuariosApiView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializador = RegistroUsuarioSerializer(data=request.data)
        validacion = serializador.is_valid()
        print(f"Resultado enviado -> {serializador.validated_data}")
        if validacion is False:
            return Response(data={
                'message': 'Error en la creacion del usuario',
                'error': serializador.errors
            })
        nuevoUsuario = UsuariosModel(**serializador.validated_data)
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        nuevoUsuario.save()
        return Response(data={
            'msg': 'Usuario creado exitosamente',
            'data': serializador.data
        }, status=201)
