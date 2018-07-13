from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class SOLICITUDES(models.Model):
	Fecha_Vigencia = models.DateField()
	Version = models.IntegerField()
	Estado = models.IntegerField()
	Centro_de_Costo = models.CharField(max_length=50)
	Documento = models.CharField(max_length=10)
	Solicitado_por = models.CharField(max_length=50)
	Fecha_Solicitud = models.DateField()
	Fecha_Requerida = models.DateField()
	CC = models.IntegerField(default=None)
	Sol = models.IntegerField(default=None)
	Item = models.IntegerField(default=None)
	Descripcion = models.CharField(max_length=100,default=None)
	Cant = models.IntegerField(default=None)
	Unid = models.IntegerField(default=None)
	Cert = models.CharField(max_length=10,default=None)
	AoD = models.CharField(max_length=20,default=None)

class BODEGUEROS(models.Model):
    Nombre = models.CharField(max_length=50)

class BODEGAS(models.Model):
    Ubicacion = models.CharField(max_length=50)
    Hoja_de_Cargo = models.CharField(max_length=200)

class MATERIALES(models.Model):
    Nombre = models.CharField(max_length=50)
    Cantidad = models.IntegerField()

class PROVEEDORES(models.Model):
    Nombre = models.CharField(max_length=50)