from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    contacto = models.CharField(max_length=10)


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)


class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=10)


class Paciente(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nombreCompleto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    tipoSangre = models.CharField(max_length=10)
    estatura = models.FloatField(max_length=10)
    diagnostico = models.CharField(max_length=50)


class Visita(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(max_length=20)
    motivo = models.CharField(max_length=100)


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

class Receta(models.Model):
   Visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
   Productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
   cantidad = models.CharField(max_length=100)
     