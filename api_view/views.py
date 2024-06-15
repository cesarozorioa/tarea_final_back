from django.shortcuts import render
from rest_framework import generics
from App1.models import ProyectoDb,UsuarioDb
from .serializer import ProyectoDbSerializer,UsuarioDbSerializer
from rest_framework import viewsets

# Create your views here.

class AutorDbViewSet(viewsets.ModelViewSet):
    queryset = ProyectoDb.objects.all()
    serializer_class = ProyectoDbSerializer

class UsuarioDbViewSet(viewsets.ModelViewSet):
    queryset = UsuarioDb.objects.all()
    serializer_class = UsuarioDbSerializer