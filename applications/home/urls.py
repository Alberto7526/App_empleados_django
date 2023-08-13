from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.IndexView.as_view()),
    path("lista" , views.PruebaListView.as_view()),
    path("lista_prueba" , views.Lista2View.as_view()),
    path("add_prueba", views.PruebaCreateView.as_view())
]