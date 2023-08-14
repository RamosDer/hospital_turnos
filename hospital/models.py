from django.db import models

class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    embarazada = models.BooleanField(default=False)
    tercera_edad = models.BooleanField(default=False)
