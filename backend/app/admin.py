# backend/app/admin.py
from django.contrib import admin
from .models import Profesor, Laboratorio, Software, Curso, HorarioAsignado

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'disponibilidad')
    search_fields = ('nombre',)

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'listar_software')
    filter_horizontal = ('software',)
    
    def listar_software(self, obj):
        return ", ".join([s.nombre for s in obj.software.all()])
    listar_software.short_description = 'Software instalado'

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'software_requerido', 'total_alumnos', 'peso')
    list_filter = ('profesor', 'software_requerido')
    search_fields = ('nombre', 'profesor__nombre')
    raw_id_fields = ('prerequisito',)

class HorarioAsignadoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'laboratorio', 'dia', 'hora_inicio')
    list_filter = ('dia', 'laboratorio')
    search_fields = ('curso__nombre', 'laboratorio__nombre')
    date_hierarchy = None

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(HorarioAsignado, HorarioAsignadoAdmin)