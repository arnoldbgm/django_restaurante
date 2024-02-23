from django.db import models

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
        to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id')

    class Meta:
        db_table = 'platos'
