# backend/app/urls.py
from django.urls import path
from .views import asignar_horarios_view, HorarioListView

urlpatterns = [
    path('asignar_horarios/', asignar_horarios_view, name='asignar_horarios'),
    path('horarios/', HorarioListView.as_view(), name='horario_list'),
]
