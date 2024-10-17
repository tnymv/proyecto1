"""
URL configuration for PUNTO_DE_VENTA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventario', include('inventario.urls')),
    path('', include('ventas.urls')),
    path('', include('compras.urls')),

    #Autenticacino 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name='password_change_done'),
    path('logout/', auth_views.LogoutView.as_view(), 
         name='logout'),
]
