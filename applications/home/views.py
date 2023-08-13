from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
      template_name = 'home/lista.html'
      queryset = ['a','b','c']
      context_object_name = 'lista_nombres'

class Lista2View(ListView):
      template_name = 'home/lista_prueba.html'
      model = Prueba
      context_object_name = 'lista_pruebas'

class PruebaCreateView(CreateView):
      template_name = 'home/create.html'
      model=Prueba
      form_class = PruebaForm
      success_url='.'