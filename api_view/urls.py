from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AutorDbViewSet,UsuarioDbViewSet
router = DefaultRouter()#definir un router
router.register('proyectos',AutorDbViewSet,basename='proyectos')
router.register('usuarios',UsuarioDbViewSet,basename='usuarios')
urlpatterns = []
urlpatterns +=router.urls