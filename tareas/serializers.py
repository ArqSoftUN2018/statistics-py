from rest_framework import serializers
from tareas.models import Tarea

class TareaSerializer(serializers.Serializer):
    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'creado_por', 'asignado_a', 'tablero', 'fecha_vencimiento', 'terminada',)