from rest_framework.permissions import BasePermission
from .models import UsuariosModel

class SoloAdministradores(BasePermission):
    message = 'Este permiso es propio de los administradores'
    def has_permission(self, request, view):
        usuario:UsuariosModel = request.user
        if usuario.tipoUsuario is 'ADMIN':
            return True
        else:
            return False