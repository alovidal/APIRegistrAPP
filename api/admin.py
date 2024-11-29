from django.contrib import admin
from .models import *

# Personalización para sedeInstitucion
@admin.register(sedeInstitucion)
class SedeInstitucionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion")  # Columnas a mostrar en la lista
    search_fields = ("nombre", "direccion")  # Campos para buscar
    list_filter = ("direccion",)  # Filtros para la barra lateral

# Personalización para usuario
@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "sede")  # Columnas visibles
    search_fields = ("username", "email", "sede__nombre")  # Búsqueda avanzada
    list_filter = ("sede",)  # Filtro para las sedes
    filter_horizontal = ("asignaturas",)  # Widget mejorado para campos ManyToMany

# Personalización para asignatura
@admin.register(asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ("nombreAsignatura", "codigo", "seccion")  # Columnas visibles
    search_fields = ("nombreAsignatura", "codigo", "seccion")  # Campos de búsqueda
    list_filter = ("seccion",)  # Filtro por sección

# Personalización para asistencia
@admin.register(asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "asignatura", "fecha", "presente")  # Columnas visibles
    search_fields = ("usuario__username", "asignatura__nombreAsignatura")  # Búsqueda
    list_filter = ("asignatura", "fecha", "presente")  # Filtros adicionales
