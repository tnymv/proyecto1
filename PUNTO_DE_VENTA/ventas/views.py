from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
# Create your views here.

def inicio(request):
    return HttpResponse("PANEL PRINCIPAL")

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') 
        else:
            return render(request, 'form_create.html', {
                'form': form, 
                'modelo': 'Cliente'
            })
    else:
        form = ClienteForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo': 'Cliente'
        })

def listar_clientes(request):
    queryset = Cliente.objects.filter(
        activo=True
    )
    clientes_data = [
        {field.name: getattr(item, field.name) for field in Cliente._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': clientes_data,
        'modelo': 'Clientes'
    })


def actualizar_cliente(request, id):
    queryset = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Cliente'
    })

def eliminar_cliente(request, id):
    queryset = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        queryset.activo = False
        queryset.save()
        return redirect('lista_clientes')
    else:
        return HttpResponse("Metodo no permitido")


def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') 
        else:
            return render(request, 'form_create.html', {
                'form': form, 
                'modelo': 'Producto'
            })
    else:
        form = ProductoForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo': 'Producto'
        })

def listar_productos(request):
    queryset = Producto.objects.filter(
        activo=True
    )
    productos_data = [
        {field.name: getattr(item, field.name) for field in Producto._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': productos_data,
        'modelo': 'Producto'
    })


def actualizar_producto(request, id):
    queryset = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Producto'
    })

def eliminar_producto(request, id):
    queryset = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        queryset.activo = False
        queryset.save()
        return redirect('lista_productos')
    else:
        return HttpResponse("Metodo no permitido")


def crear_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        formset = PedidoProductoFormSet(request.POST)
        
        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save(commit=False)
            precio_total = 0

            for form in formset:
                cantidad = form.cleaned_data.get('cantidad')
                precio = form.cleaned_data.get('precio')
                if cantidad and precio:
                    precio_total += cantidad * precio
            
            pedido.precio_total = precio_total

            pedido.save()

            formset.instance = pedido
            formset.save()

            return redirect('lista_pedidos')
    else:
        pedido_form = PedidoForm()
        formset = PedidoProductoFormSet()

    return render(request, 'crear_pedido.html', {
        'pedido_form': pedido_form,
        'formset': formset,
    })

def listar_pedidos(request):
    queryset = Pedido.objects.all()
    pedidos_data = [
        {field.name: getattr(item, field.name) for field in Pedido._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': pedidos_data,
        'modelo': 'Pedidos'
    })

def obtener_precio_producto(request, producto_id):
    producto = Producto.objects.filter(id=producto_id, activo=True).first()
    if producto:
        return JsonResponse({'precio': str(producto.precio_venta)})
    return JsonResponse({'precio': '0.00'}, status=404)


def detalle_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    productos = PedidoProducto.objects.filter(pedido=pedido)

    if request.method == 'POST':
        form = DespacharPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = DespacharPedidoForm(instance=pedido)

    return render(request, 'detalle_pedido.html', {
        'pedido': pedido,
        'productos': productos,
        'form': form
    })