"""
URL configuration for genb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers

from pacientes import views
from pacientes.views import (agregar_paciente, ver_paciente, eliminar_paciente, modificar_paciente, generar_reporte,
                             PacienteViewSet,EspecialidadViewSet )
from webapp.views import bienvenida, bienvenida2, despedida, mostrar_edad



router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'especialidad', EspecialidadViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bienvenido/', bienvenida),
    #path('despedida/', despedida),
    path('', bienvenida2, name = 'inicio'),
    path('agregar_paciente/', agregar_paciente),
    path('ver_paciente/<int:id>',ver_paciente),
    path('eliminar_paciente/<int:id>',eliminar_paciente),
    path('modificar_paciente/<int:id>',modificar_paciente),
    path('generar_reporte/', generar_reporte),
    #path('mostrar_edad/<int:id>',mostrar_edad),
]

urlpatterns += router.urls

