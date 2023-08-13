from django.contrib import admin
from .models import Empleado,Cargos,Habilidades
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'cargo',
        'departamento',
        'full_name',)
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name
    search_fields = ('first_name','last_name',)
    list_filter = ('departamento','cargo')
    
    # agregar un filtro horizontal para las habilidades
    filter_horizontal = ('Habilidades',)
    
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Habilidades)
admin.site.register(Cargos)