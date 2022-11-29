from django.db import models

class Alumnos(models.Model):
    Nombre = models.CharField(max_length=150)
    ApellidoP = models.CharField(max_length=150)
    ApellidoM = models.CharField(max_length=150)
    Correo = models.CharField(max_length=150)
    Contraseña = models.CharField(max_length=150)

class Maestro(models.Model):
    Nombre = models.CharField(max_length=150)
    ApellidoP = models.CharField(max_length=150)
    ApellidoM = models.CharField(max_length=150)
    Correo = models.CharField(max_length=150)
    Contraseña = models.CharField(max_length=150)

class Carrera(models.Model):
    Nombre_Carrera = models.CharField(max_length=150)
    Materia1 = models.CharField(max_length=150)
    Materia2 = models.CharField(max_length=150)
    Materia3 = models.CharField(max_length=150)
    Materia4 = models.CharField(max_length=150)
    Materia5 = models.CharField(max_length=150)

class Horario(models.Model):
    Nombre = models.CharField(max_length=150)
    ApellidoP = models.CharField(max_length=150)
    ApellidoM = models.CharField(max_length=150)
    Nombre_Carrera = models.CharField(max_length=150)
    Materia1H = models.CharField(max_length=150)
    Materia2H = models.CharField(max_length=150)
    Materia3H = models.CharField(max_length=150)
    Materia4H = models.CharField(max_length=150)
    Materia5H = models.CharField(max_length=150)

class Materias(models.Model):
    Nombre = models.CharField(max_length=150)
    ApellidoP = models.CharField(max_length=150)
    ApellidoM = models.CharField(max_length=150)
    Nombre_Carrera = models.CharField(max_length=150)
    Nombre_Materia = models.CharField(max_length=150)


