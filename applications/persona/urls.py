from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path("",
         views.InicioView.as_view(),
         name = 'inicio'),
    path("list-all/",
         views.ListAllEmpleados.as_view(),
         name='empleados_all'
         ),
    path("list-empleados-edit/",
         views.ListByKwordEdit.as_view(),
         name='empleados_edit'
         ),
    path("list-by-area/<shortName>/",
         views.ListByArea.as_view(),
         name='empleado_area'),
    path("list-by-kword",views.ListByKword.as_view()),
    path("add-empleado/",
         views.EmpleadoCreateView.as_view(),
         name='empleado-add'),
    path("update-empleado/<pk>/",
         views.EmpleadoUpdateview.as_view(),
         name='empleado-edit'),
    path("delete-empleado/<pk>/",
         views.EmpleadoDeleteView.as_view(),
         name='eliminar_empleado'),
    path("ver_empleado/<pk>/",
         views.EmpleadoDetailView.as_view(),
         name='Detalle_empleado')
]