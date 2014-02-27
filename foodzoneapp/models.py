from django.db import models

#Zona
class Zona(models.Model):
    descripcion = models.CharField(max_length = 50)
    latitud = models.FloatField()
    longitud = models.FloatField()
    activo = models.BooleanField(default = True)



#Tipo de Local Ejemplo: Bar, Restaurante, Quiosco
class TipoLocal(models.Model):
    tipos = ((1,'Bar'), (2,'Restaurante'), (3,'Quiosco'))
    #id_tipo = models.SmallIntegerField(primary_key = True, choices = tipos, default = 1)
    descripcion = models.CharField(max_length = 60)



#Local    
class Local(models.Model):
    nombre = models.CharField(max_length = 30)
    tipo_local = models.ForeignKey(TipoLocal)
    direccion = models.CharField(max_length = 50)
    resena = models.CharField(max_length = 60)
    latitud = models.FloatField()
    longitud = models.FloatField()
    activo = models.BooleanField(default = True)
    up = models.IntegerField(default = 0)
    down = models.IntegerField(default = 0)
    fechaIngreso = models.DateTimeField("Fecha de Ingreso")
    userIngreso = models.IntegerField()



#Plato
class Plato(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 50)
    up = models.IntegerField(default = 0)
    down = models.IntegerField(default = 0)
    fechaIngreso = models.DateTimeField("Fecha de Ingreso")
    precio = models.FloatField()
    id_local = models.ForeignKey(Local)
    
    #Debe ser nullable porque hay la posibilidad de no subir foto.
    #image = models.ImageField(upload_to='image/platos/', null=True)
