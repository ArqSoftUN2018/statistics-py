from rest_framework import serializers
from estadisticas.models import Estadistica

class EstadisticaSerializer(serializers.Serializer):
    class Meta:
        model = Estadistica
        fields = ('id', 'nombre', 'creado_por', 'tipo_reporte',)