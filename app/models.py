from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    dpto = models.CharField(max_length=10, null=False, blank=False)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.OneToOneField('estudiante', unique=True, blank=False, null=False, on_delete=models.CASCADE)
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.CharField(max_length=50, null=False, blank=False)
    profesor = models.ManyToManyField('profesor')
    estudiante = models.ManyToManyField('estudiante')
    
    def __str__(self):
        return f'{self.codigo} - {self.nombre}, v:{self.version}'