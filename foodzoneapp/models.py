from django.db import models

# Create your models here.

class Zona(models.Model):
    descripcion = models.CharField(max_length = 50)
    latitud = models.FloatField()
    longitud = models.FloatField()
    activo = models.BooleanField(default = True)

class TipoLocal(models.Model):
    descripcion = models.CharField(max_length = 60)
    
class Local(models.Model):
    nombre = models.CharField(max_length = 30)
    tipo_local = models.ForeignKey(TipoLocal)
    direccion = models.CharField(max_length = 50, blank = True)
    resena = models.CharField(max_length = 60, blank = True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    activo = models.BooleanField(default = True)
    up = models.IntegerField(default = 0)
    down = models.IntegerField(default = 0)
    fechaIngreso = models.DateTimeField("Fecha de Ingreso")
    userIngreso = models.IntegerField()

class Plato(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 50)
    up = models.IntegerField(default = 0)
    down = models.IntegerField(default = 0)
    fechaIngreso = models.DateTimeField("Fecha de Ingreso")
    precio = models.FloatField()
    id_local = models.ForeignKey(Local)
