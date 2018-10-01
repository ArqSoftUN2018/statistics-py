from django.db import models

class Estadistica(models.Model):
	nombre = models.CharField(max_length = 100)
	creado_por = models.CharField(max_length = 100)
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	tipo_reporte = models.IntegerField()