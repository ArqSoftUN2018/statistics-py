from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estadisticas.models import Estadistica
from estadisticas.serializers import EstadisticaSerializer

@api_view(['GET', 'POST'])
def estadistica_list(request, format = None):
    if request.method == 'GET':
        estadisticas = Estadistica.objects.all()
        serializer = EstadisticaSerializer(estadisticas, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EstadisticaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def estadistica_detail(request, pk, format = None):
    try:
        estadistica = Estadistica.objects.get(pk = pk)
    except Estadistica.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstadisticaSerializer(estadistica)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EstadisticaSerializer(estadistica, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estadistica.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)