from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    edad = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    
    # Agrega los atributos related_name a las relaciones
    groups = models.ManyToManyField('auth.Group', related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users')

    def __str__(self):
        return self.username
