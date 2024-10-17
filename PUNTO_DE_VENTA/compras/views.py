from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proveedor
from .forms import *

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores') 
        else:
            return render(request, 'form_create.html', {
                'form': form, 
                'modelo': 'Proveedor'
            })
    else:
        form = ProveedorForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo': 'Proveedor'
        })


def listar_proveedores(request):
    queryset = Proveedor.objects.all()
    proveedores_data = [
        {field.name: getattr(item, field.name) for field in Proveedor._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': proveedores_data,
        'modelo': 'Proveedor'
    })


def actualizar_proveedor(request, id):
    queryset = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Proveedor'
    })


def eliminar_proveedor(request, id):
    queryset = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_proveedores')
    else:
        return HttpResponse("Método no permitido")
    
    
def listar_pedidos(request):
    queryset = OrdenCompra.objects.all()
    pedidos_data = [
        {field.name: getattr(item, field.name) for field in OrdenCompra._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': pedidos_data,
        'modelo': 'OrdenCompra'
    })
    
def crear_orden_compra(request):
    if request.method == 'POST':
        orden_form = OrdenCompraForm(request.POST)
        formset = OrdenCompraProductoFormSet(request.POST, instance=orden_form.instance)
        
        if orden_form.is_valid() and formset.is_valid():
            orden = orden_form.save()
            formset.instance = orden
            formset.save()
            return redirect('lista_ordenes')
    else:
        orden_form = OrdenCompraForm()
        formset = OrdenCompraProductoFormSet()

    return render(request, 'crear_orden_compra.html', {
        'orden_form': orden_form,
        'formset': formset
    })
    
    
def detalle_orden_compra(request, id):
    orden = get_object_or_404(OrdenCompra, id=id)
    productos = OrdenCompraProducto.objects.filter(orden=orden)

    if request.method == 'POST':
        form = OrdenCompraForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes_compra')
    else:
        form = OrdenCompraForm(instance=orden)

    return render(request, 'detalle_orden.html', {
        'orden': orden,
        'productos': productos,
        'form': form
    })
