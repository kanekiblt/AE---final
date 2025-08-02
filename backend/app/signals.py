from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import HorarioAsignado
import logging

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=HorarioAsignado)
def validar_horario(sender, instance, **kwargs):
    """
    Valida las restricciones básicas antes de guardar un horario
    """
    if instance.curso.software_requerido not in instance.laboratorio.software.all():
        logger.warning(f"El laboratorio no tiene el software requerido para {instance.curso}")
    
    if instance.curso.total_alumnos > instance.laboratorio.capacidad:
        logger.error(f"Capacidad excedida en {instance.laboratorio} para {instance.curso}")

@receiver(post_save, sender=HorarioAsignado)
def notificar_nuevo_horario(sender, instance, created, **kwargs):
    """
    Ejemplo: Notificar cuando se crea un nuevo horario
    """
    if created:
        logger.info(f"Nuevo horario creado: {instance}")
