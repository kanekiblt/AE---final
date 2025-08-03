# backend/app/models.py
from django.db import models
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    disponibilidad = models.JSONField(default=list) 

    def __str__(self):
        return self.nombre
    
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    software = models.ManyToManyField("Software")
    disponibilidad = models.JSONField(default=list)
      

    def __str__(self):
        return self.nombre

class Software(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre  = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    peso = models.IntegerField()  #Se usa para la jerarquia
    software_requerido = models.ForeignKey(Software, on_delete=models.CASCADE)
    duracion_hora = models.IntegerField(default=1)
    total_alumnos = models.IntegerField()
    prerequisito = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class HorarioAsignado(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    dia = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.curso.nombre} en {self.laboratorio.nombre} el {self.dia} a las {self.hora_inicio}"

    