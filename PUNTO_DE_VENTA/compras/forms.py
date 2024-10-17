# forms.py
from django import forms
from .models import *
from django.forms import inlineformset_factory


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'contacto_principal', 'telefono', 'direccion']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el nombre de la empresa'
            }),
            'contacto_principal': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el nombre del contacto principal'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el número de teléfono'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese la dirección',
                'rows': 3
            }),
        }

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = ['numero_orden', 'proveedor', 'estado_orden']
        widgets = {
            'numero_orden': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Orden'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'estado_orden': forms.Select(attrs={'class': 'form-control'}),
        }

class OrdenCompraProductoForm(forms.ModelForm):
    class Meta:
        model = OrdenCompraProducto
        fields = ['producto', 'cantidad', 'precio_compra']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control'}),
        }


OrdenCompraProductoFormSet = inlineformset_factory(
    OrdenCompra,
    OrdenCompraProducto,
    form=OrdenCompraProductoForm,
    extra=1,
    can_delete=True
)
