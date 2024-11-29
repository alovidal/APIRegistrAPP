from rest_framework import serializers
from .models import *

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = asignatura
        fields = "__all__"

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = asistencia
        fields = "__all__"
        
class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = sedeInstitucion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True)
    class Meta:
        model = usuario
        fields= ["username", "email", "password", "sede", "asignaturas"]        