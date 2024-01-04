from rest_framework import serializers


from pacientes.models import Paciente, Especialidad, Doctor


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ('url','nombre', 'apellido', 'sexo', 'email', 'activo', 'especialidad')

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('url','nombre', 'doctor')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('url','especialidad', 'nombre','email')
