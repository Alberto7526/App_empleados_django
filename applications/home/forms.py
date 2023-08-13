from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        # aca se personalizan los campos
        widgets = {
            'cantidad':forms.NumberInput(
                attrs={
                    'placeholder':'Ingrese un numero mayor a 10'
                }
            )
        }
    
    def clean_cantidad(self):
        '''
        Esta funcion permite validar los parametros de mi formulario 
        para este caso vlidaremos que cantidad sea mayor que 10
        '''
        
        cantidad = self.cleaned_data['cantidad']
        
        if not(cantidad.isdigit()):
            raise forms.ValidationError('Por favor ingrese un numero')    
        
        if int(cantidad) < 10:
            raise forms.ValidationError('Por favor ingrese un  numero mayor o igual a 10')
        
        return cantidad
    