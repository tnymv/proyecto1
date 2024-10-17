from django.db import models
from ventas.models import *

# Create your models here.
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_empresa


class OrdenCompra(models.Model):
    numero_orden = models.CharField(max_length=20, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    estado_orden = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('recibida', 'Recibida'),
        ('cancelada', 'Cancelada')
    ], default='pendiente')
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Orden {self.numero_orden}'

class OrdenCompraProducto(models.Model):
    orden = models.ForeignKey('OrdenCompra', on_delete=models.CASCADE)
    producto = models.ForeignKey('ventas.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre_producto}'