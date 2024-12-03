from django.urls import path, include
from rest_framework import routers
from api import views
from .views import *

routers = routers.DefaultRouter()
routers.register(r'usuarios', views.UsuarioViewSet)
routers.register(r'asignaturas', views.AsignaturaViewSet)
routers.register(r'asistencia', views.AsistenciaViewSet)
routers.register(r'sedes', views.SedeViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]