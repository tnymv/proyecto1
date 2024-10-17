from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('lista_proveedores/', views.listar_proveedores, name='lista_proveedores'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    
     path('lista_ordenes/', views.listar_pedidos, name='lista_ordenes'),

    # Ruta para crear una nueva orden de compra
    path('nueva_orden/', views.crear_orden_compra, name='nueva_orden'),

    # Ruta para ver el detalle de una orden de compra específica
    path('detalle_orden/<int:id>/', views.detalle_orden_compra, name='detalle_orden'),
]