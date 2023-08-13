from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path("new-dep/",
         views.NewDepartamentoView.as_view(),
         name = 'new_departamento'),
    path("list_departamento/",
         views.ListAllEmpleados.as_view(),
         name = 'list_all_departamento')
]