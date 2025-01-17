# Generated by Django 5.1.2 on 2024-10-16 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('contacto_principal', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.CharField(max_length=20, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado_orden', models.CharField(choices=[('pendiente', 'Pendiente'), ('recibida', 'Recibida'), ('cancelada', 'Cancelada')], max_length=50)),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor')),
            ],
        ),
    ]
