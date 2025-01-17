# Generated by Django 3.2 on 2024-10-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_alter_pedido_estado_pedido'),
        ('compras', '0002_proveedor_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='costo_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_orden',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('recibida', 'Recibida'), ('cancelada', 'Cancelada')], default='pendiente', max_length=50),
        ),
        migrations.CreateModel(
            name='OrdenCompraProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.ordencompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
    ]
