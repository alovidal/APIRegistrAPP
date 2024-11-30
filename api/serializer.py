from rest_framework import serializers
from .models import *

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = "__all__"

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = "__all__"
        
class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedeInstitucion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True)
    class Meta:
        model = Usuario
        fields= ["username", "email", "password", "sede", "asignaturas"]        