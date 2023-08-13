from django import forms 
from .models import Empleado

class EmpleadoForm (forms.ModelForm):
    class Meta:
        model =Empleado
        fields = {
        'first_name',
        'last_name',
        'cargo',
        'departamento',
        'Habilidades',
        'avatar'
        }
        # permite personalizadr la selecciíon de las habilidades 
        widgets = {
           'Habilidades' : forms.CheckboxSelectMultiple()
        }