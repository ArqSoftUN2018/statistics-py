from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reportes.models import Reporte
from reportes.serializers import ReporteSerializer

@api_view(['GET', 'POST'])
def reporte_list(request, format = None):
    if request.method == 'GET':
        reportes = Reporte.objects.all()
        serializer = ReporteSerializer(reportes, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReporteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reporte_detail(request, pk, format = None):
    try:
        reporte = Reporte.objects.get(pk = pk)
    except Reporte.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReporteSerializer(reporte)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReporteSerializer(reporte, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reporte.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)