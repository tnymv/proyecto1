# forms.py
from django import forms
from .models import *
from django.forms import inlineformset_factory

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_completo','direccion', 'telefono', 'correo_electronico']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control','type': 'email', 'placeholder': 'Ingrese correo electronico'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo_producto', 
            'nombre_producto', 
            'descripcion', 
            'precio_venta', 
            'precio_compra', 
            'cantidad_inventario', 
            'proveedor', 
            'categoria'
        ]
        widgets = {
            'codigo_producto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el código del producto'
            }),
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese la descripción', 
                'rows': 3
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el precio de venta'
            }),
            'precio_compra': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el precio de compra'
            }),
            'cantidad_inventario': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese la cantidad en inventario', 
                'min': 0
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'cliente']
        widgets = {
            'numero_pedido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Pedido'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }


class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad', 'precio']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

PedidoProductoFormSet = inlineformset_factory(
    Pedido,
    PedidoProducto,
    form=PedidoProductoForm,
    extra=1,
    can_delete=True
)

class DespacharPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado_pedido']
        widgets = {
            'estado_pedido': forms.Select(attrs={'class': 'form-control'}),
        }