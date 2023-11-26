from django.forms import ModelForm, EmailInput

from pacientes.models import Paciente


class PacienteFormulario(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'sexo', 'email', 'activo','especialidad')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }