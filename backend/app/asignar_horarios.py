from django.core.management.base import BaseCommand
from app.asignadorGenetico import asignar_horarios_geneticos  # ← Corrección aquí

class Command(BaseCommand):
    help = 'Asigna horarios a los cursos en los laboratorios disponibles'

    def handle(self, *args, **kwargs):
        asignar_horarios_geneticos() 
        self.stdout.write(self.style.SUCCESS('Horarios asignados correctamente.'))
