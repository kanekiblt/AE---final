# backend/app/serializers.py
from rest_framework import serializers
from .models import Profesor, Curso, Laboratorio, Software, HorarioAsignado

class profesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class softwareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Software
        fields = '__all__'

class laboratorioSerializer(serializers.ModelSerializer):
    software = softwareSerializer(many=True, read_only=True)

    class Meta:
        model = Laboratorio
        fields = '__all__'

class cursoSerializer(serializers.ModelSerializer):
    Profesor = profesorSerializer(read_only=True)
    software_requerido = softwareSerializer(read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'

class horarioAsignadoSerializer(serializers.ModelSerializer):
    curso = cursoSerializer(read_only=True)
    Laboratorio = laboratorioSerializer(read_only=True)

    class Meta:
        model = HorarioAsignado
        fields = '__all__'
    
