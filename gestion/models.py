from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager
# Create your models here.


class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=25, unique=True)

    # Definimos los atributos de la clase o metadatos
    class Meta:
        db_table = 'categorias'
        ordering = ['nombre']  # Ordenamiento del nombre de forma asc


class PlatoModel(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')
    # Permite evitar la eliminacion de la categoria si es que tiene datos que dependen de ella
    categoria = models.ForeignKey(
        to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')

    class Meta:
        db_table = 'platos'


# Aqui vamos a modificar el comportamiento de la talba de usuarios de django
class UsuariosModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido_paterno = models.CharField(max_length=50, null=False)
    apellido_materno = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=100, null=False, unique=True)
    # Debe llamarse necesriamente password no puedes poner pass ni contraseñita
    password = models.TextField(max_length=100, null=False)
    # El primeero es con el que se va
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('MOZO', 'MOZO'),
        ('CLIENTE', 'CLIENTE')
    ])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno',
                       'apellido_materno', 'tipoUsuario']
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'
