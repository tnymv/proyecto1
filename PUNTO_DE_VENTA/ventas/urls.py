from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('lista_clientes/', views.listar_clientes, name='lista_clientes'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'), 

    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('lista_productos/', views.listar_productos, name='lista_productos'),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'), 

      # Rutas para la gestión de pedidos
    path('nuevo_pedido/', views.crear_pedido, name='crear_pedido'),
    path('lista_pedidos/', views.listar_pedidos, name='lista_pedidos'),
    path('api/producto/<int:producto_id>/precio/', views.obtener_precio_producto, name='obtener_precio_producto'),
    # path('actualizar_pedido/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    # path('eliminar_pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
    # Rutas para pedidos
    path('lista_pedidos/', views.listar_pedidos, name='lista_pedidos'),
    path('detalle_pedido/<int:id>/', views.detalle_pedido, name='detalle_pedido'),
]