# backend/management/commands/asignar_horarios.py
from django.core.management.base import BaseCommand
from backend.app.asignadorGenetico import asignadorGenetico
class Command(BaseCommand):
    help = 'Asigna horarios a los cursos en los laboratorios disponibles'

    def handle(self, *args, **kwargs):
        asignadorGenetico()
        self.stdout.write(self.style.SUCCESS('Horarios asignados correctamente.'))
