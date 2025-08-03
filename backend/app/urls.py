# backend/app/aurls.py
from django.urls import path
from .views import HorarioListView, GenerarHorariosView, HorarioDetailView

urlpatterns = [
    path('horarios/', HorarioListView.as_view(), name='horario-list'),
    path('horarios/generar/', GenerarHorariosView.as_view(), name='generar-horarios'),
    path('horarios/<int:pk>/', HorarioDetailView.as_view(), name='horario-detail'),
]
