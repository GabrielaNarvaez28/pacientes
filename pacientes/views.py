from django.forms import modelform_factory
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from pacientes.forms import PacienteFormulario
from pacientes.models import Paciente

# Create your views here.

#PacienteFormulario = modelform_factory(Paciente, exclude=['activo',])
def agregar_paciente(request):
    pagina = loader.get_template('pacientes/agregar.html')
    if request.method == 'GET':
        formulario = PacienteFormulario
    elif request.method == 'POST':
        formulario = PacienteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos,request))

def modificar_paciente(request, id):
    pagina = loader.get_template('pacientes/modificar.html')
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'GET':
        formulario = PacienteFormulario(instance=paciente)
    elif request.method == 'POST':
        formulario = PacienteFormulario(request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_paciente(request, id):
    # paciente = Paciente.objects.get(pk=id)
    paciente = get_object_or_404(Paciente, pk=id)
    datos = {'paciente':paciente}
    # print(paciente)
    pagina = loader.get_template('pacientes/ver.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if paciente:
        paciente.delete()
        return redirect('inicio')









