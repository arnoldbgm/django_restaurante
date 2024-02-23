# Generated by Django 5.0.2 on 2024-02-23 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('categoria', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.PROTECT, to='gestion.categoria')),
            ],
            options={
                'db_table': 'platos',
            },
        ),
    ]