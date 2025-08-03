# backend/app/serializers.py

from rest_framework import serializers
from .models import HorarioAsignado, Curso, Laboratorio, Profesor, Software

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'disponibilidad']

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = ['id', 'nombre']

class LaboratorioSerializer(serializers.ModelSerializer):
    software = SoftwareSerializer(many=True)
    
    class Meta:
        model = Laboratorio
        fields = ['id', 'nombre', 'capacidad', 'software']

class CursoSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer()
    software_requerido = SoftwareSerializer()
    
    class Meta:
        model = Curso
        fields = [
            'id', 'nombre', 'profesor', 'peso', 
            'software_requerido', 'total_alumnos', 'prerequisito'
        ]

class HorarioAsignadoSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    laboratorio = LaboratorioSerializer()
    
    class Meta:
        model = HorarioAsignado
        fields = ['id', 'curso', 'laboratorio', 'dia', 'hora_inicio']
        depth = 1

class CreateHorarioAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioAsignado
        fields = ['curso', 'laboratorio', 'dia', 'hora_inicio']