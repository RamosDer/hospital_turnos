from django.db import models
from hospital.models import Paciente, Medico

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    prioridad = models.PositiveIntegerField(default=0)
