from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DeleteView, TemplateView, DetailView
from .models import Empleado 
from django.urls import reverse_lazy
from .forms import EmpleadoForm
# Create your views here.
class InicioView(TemplateView):
    '''
    Carga la pagina de inicio de la aplicación 
    '''
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    '''
    Esta función permite consultar de la base de datos todos los empleados existentes
    y los muestra en forma de lista en el template list_all.html
    
    En el template se registran los datos por medio de la variable object_list
    
    '''
    template_name = 'persona/list_all.html'
    paginate_by = 6
    ordering = 'first_name'
    model = Empleado
    
    def get_queryset(self):
        '''
        La variable palabra clave permite captuar del metodo GET el atributo remarcado con 
        el identificador kword
        '''
        palabra_clave = self.request.GET.get("kword",'') # captura de la palaba clave utilizando el identificador kword        #filtro
        lista = Empleado.objects.filter(
            full_name__icontains =palabra_clave
        )
        
        return lista
    
class ListByArea(ListView):
    '''
    Esta función permite recibir el area por la url y ejecuta un filtro 
    de los empleados según el area
    '''
    template_name = 'persona/list_by_area.html'
    
    def get_queryset(self):
        '''
        esta es la función que jecuta el filtro
        '''
        area = self.kwargs['shortName']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista
    
class ListByKword(ListView):
    '''
    Esta función permite hacer realizar el filtro utilizando una petición get
    esta petición se envía desde el navegador utilizando "form" en el HTML 
    '''
    template_name = 'persona/list_kword.html'
    
    
    def get_queryset(self):
        '''
        La variable palabra clave permite captuar del metodo GET el atributo remarcado con 
        el identificador kword
        '''
        palabra_clave = self.request.GET.get("kword",'') # captura de la palaba clave utilizando el identificador kword
        print('La palabra capturada por el metodo Get---------{}--------------'.format(palabra_clave))
        #filtro
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        
        return lista
    
class ListByKwordEdit(ListView):
    '''
    Esta función permite hacer realizar el filtro utilizando una petición get
    esta petición se envía desde el navegador utilizando "form" en el HTML 
    '''
    template_name = 'persona/list_empleado.html'
    paginate_by = 8
    
    def get_queryset(self):
        '''
        La variable palabra clave permite captuar del metodo GET el atributo remarcado con 
        el identificador kword
        '''
        palabra_clave = self.request.GET.get("kword",'') # captura de la palaba clave utilizando el identificador kword
        #filtro
        lista = Empleado.objects.filter(
            full_name__icontains =palabra_clave
        )
        
        return lista

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add-empleado.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all')
    
    def form_valid(self, form):
        '''
        Esta función permite interceptar los datos que se van a guardar para el nuevo registro 
        y realizar acciones adicionales, en este caso permite guardar el dato full_name
        utilizando los datos ingresados 
        '''
        empleado  = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateview(UpdateView):
    template_name = 'persona/update.html'
    model=Empleado
    form_class = EmpleadoForm
    #success_url = reverse_lazy('persona_app:empleados_edit')
    def form_valid(self, form):
        '''
        Esta función permite interceptar los datos que se van a guardar para el nuevo registro 
        y realizar acciones adicionales, en este caso permite guardar el dato full_name
        utilizando los datos ingresados 
        '''
        empleado  = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' '+empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateview,self).form_valid(form)
    
    def get_success_url(self):
        
        return reverse_lazy('persona_app:empleados_edit')
    
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_edit')
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = 'empleado'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado = self.get_object()
        context['Habilidades'] = empleado.Habilidades.all()
        return context