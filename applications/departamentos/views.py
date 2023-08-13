from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentForm
from applications.persona.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy


class NewDepartamentoView(FormView):
    template_name = 'departamentos/new.html'
    form_class = NewDepartamentForm
    success_url = reverse_lazy('departamento_app:list_all_departamento')
    
    def form_valid(self, form):
        nombres = form.cleaned_data['nombres']
        apellidos = form.cleaned_data['apellidos']
        departamento = form.cleaned_data['departamento']
        shortname = form.cleaned_data['shortname']
        
        depa = Departamento (
            name = departamento,
            short_name = shortname
        )
        depa.save()
        
        Empleado.objects.create(
            first_name = nombres,
            last_name = apellidos,
            departamento = depa
        )
        print (nombres,apellidos,departamento, shortname)
        return super(NewDepartamentoView,self).form_valid(form)

class ListAllEmpleados(ListView):
    '''
    Esta función permite consultar de la base de datos todos los departamentos existentes
    
    '''
    template_name = 'departamentos/list_all.html'
    paginate_by = 6
    ordering = 'id'
    model = Departamento
    