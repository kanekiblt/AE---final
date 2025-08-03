from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HorarioAsignado, Curso, Laboratorio
from .serializers import HorarioAsignadoSerializer, CreateHorarioAsignadoSerializer  
from .asignadorGenetico import asignar_horarios_geneticos
from django.db import transaction

class HorarioListView(generics.ListAPIView):
    serializer_class = HorarioAsignadoSerializer
    
    def get_queryset(self):
        return HorarioAsignado.objects.select_related(
            'curso', 'laboratorio', 'curso__profesor', 'curso__software_requerido'
        ).all()

class GenerarHorariosView(APIView):
    @transaction.atomic
    def post(self, request):
        try:
            # Limpiar horarios existentes
            HorarioAsignado.objects.all().delete()
            
            # Generar nuevos horarios
            horarios_generados = asignar_horarios_geneticos()
            
            horarios_creados = []
            for horario in horarios_generados:
                serializer = CreateHorarioAsignadoSerializer(data=horario)  
                if serializer.is_valid():
                    horario_obj = serializer.save()
                    horarios_creados.append(horario_obj)
                else:
                    raise Exception(serializer.errors)
            
            return Response({
                "status": "success",
                "message": f"{len(horarios_creados)} horarios generados correctamente",
                "data": HorarioAsignadoSerializer(horarios_creados, many=True).data
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class HorarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HorarioAsignado.objects.all()
    serializer_class = HorarioAsignadoSerializer
