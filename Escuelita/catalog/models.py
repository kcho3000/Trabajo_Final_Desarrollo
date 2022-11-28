from django.db import models

class Alumnos(models.Model):
    Nombre = models.CharField(max_length=150)
    ApellidoP = models.CharField(max_length=150)
    ApellidoM = models.CharField(max_length=150)
    Correo = models.CharField(max_length=150)
    Contraseña = models.CharField(max_length=150)
    