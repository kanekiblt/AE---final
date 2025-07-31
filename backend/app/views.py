# backend/app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HorarioAsignado 
from .serializers import horarioAsignadoSerializer
from services.asignadorGenetico import asignar_horarios

class AsignadorHorariosView(APIView):
    def post(self, request):
        asignar_horarios()  # Llama a la función para asignar horarios
        return Response({"message": "Horarios asignados correctamente."}, status=status.HTTP_200_OK)    
    
    class HorarioListView(APIView):
        def get(self, request):
            horarios = HorarioAsignado.objects.all()
            serializer = horarioAsignadoSerializer(horarios, many=True)
            return Response(serializer.data)

  
        
