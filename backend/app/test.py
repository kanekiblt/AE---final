# backend/app/test.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Profesor, Laboratorio, Software, Curso

class HorarioTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Crear datos de prueba
        self.software = Software.objects.create(nombre="Python")
        self.profesor = Profesor.objects.create(
            nombre="Dr. Smith",
            disponibilidad=["Lunes-08:00", "Martes-10:00"]
        )
        self.laboratorio = Laboratorio.objects.create(
            nombre="Lab 1",
            capacidad=30
        )
        self.laboratorio.software.add(self.software)
        
        self.curso = Curso.objects.create(
            nombre="Programación Avanzada",
            profesor=self.profesor,
            software_requerido=self.software,
            total_alumnos=25,
            peso=5
        )

    def test_generar_horarios(self):
        url = reverse('generar-horarios')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('data', response.data)

    def test_listar_horarios(self):
        url = reverse('horario-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_crear_curso(self):
    #     curso_data = {
    #         "nombre": "Inteligencia Artificial",
    #         "profesor": self.profesor.id,
    #         "software_requerido": self.software.id,
    #         "total_alumnos": 20,
    #         "peso": 4
    #     }
    #     url = reverse('admin:app_curso_add')
    #     self.client.force_login(self.profesor)  # Requiere autenticación
    #     response = self.client.post(url, curso_data)
    #     self.assertEqual(response.status_code, status.HTTP_302_FOUND)  # Redirección después de crear
    #     self.assertTrue(Curso.objects.filter(nombre="Inteligencia Artificial").exists())

class ModelTests(TestCase):
    def test_crear_profesor(self):
        profesor = Profesor.objects.create(nombre="Dr. Johnson")
        self.assertEqual(profesor.__str__(), "Dr. Johnson")

    def test_crear_laboratorio(self):
        lab = Laboratorio.objects.create(nombre="Lab 2", capacidad=25)
        self.assertEqual(lab.__str__(), "Lab 2")

    def test_curso_str(self):
        software = Software.objects.create(nombre="Java")
        profesor = Profesor.objects.create(nombre="Dr. Williams")
        curso = Curso.objects.create(
            nombre="POO",
            profesor=profesor,
            software_requerido=software,
            total_alumnos=20,
            peso=3
        )
        self.assertEqual(curso.__str__(), "POO")