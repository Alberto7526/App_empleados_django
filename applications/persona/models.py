from django.db import models
from applications.departamentos.models import Departamento
# Create your models here.
class Habilidades(models.Model):
    '''
    Modelo para tabla habilidades
    '''
    habilidad = models.CharField('Habilidad',max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de los empleados'
    
    def __str__(self):
        return str(self.id)+'- '+ self.habilidad

class Cargos(models.Model):
    '''
    Modelo para tabla cargo
    '''
    cargo = models.CharField('Cargo',max_length=50)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos de los empleados'
    
    def __str__(self):
        return str(self.id)+'- '+ self.cargo

class Empleado(models.Model):
    '''
    Modelo para tabla empleado
    '''
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, blank=True , null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', null=True, blank=True)
    Habilidades = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name','last_name']
        unique_together = ['first_name','last_name']
    
    def __str__(self):
        return str(self.id)+'- '+self.first_name + ' ' + self.last_name 