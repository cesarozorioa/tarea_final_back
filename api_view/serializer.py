from rest_framework import serializers
from App1.models import ProyectoDb,UsuarioDb

class ProyectoDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoDb
        fields = '__all__'
class UsuarioDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDb
        fields = '__all__'