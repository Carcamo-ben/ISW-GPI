from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class SOLICITUDES(models.Model):
    Fecha_Vigencia = models.DateField()
    Version = models.IntegerField()
    Estado = models.IntegerField()
    Centro_de_Costo = models.CharField(max_lenght=50)
    Documento = models.CharField(max_lenght=10)
    Solicitado_por = models.CharField(max_lenght=50)
    Fecha_Solicitud = models.DateField()
    Fecha_Requerida = models.DateField()

class SOLICITUDES2(models.Model):
	CC = models.IntegerField()
	Sol = models.IntegerField()
	Item = models.IntegerField()
	Descripcion = models.CharField(max_length=100)
	Cant = models.IntegerField()
	Unid = models.IntegerField()
	Cert = models.CharField(max_length=10)
	AoD = models.CharField(max_length=20)

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