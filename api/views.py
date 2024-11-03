from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Campos que se pueden filtrar
    filterset_fields = ["username","password", ]