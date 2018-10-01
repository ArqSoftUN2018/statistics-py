from django.db import models


class Tarea(models.Model):
	nombre = models.CharField(max_length = 100)
	creado_por = models.CharField(max_length = 100)
	asignado_a = models.CharField(max_length = 100)
	tablero = models.CharField(max_length = 100)
	fecha_vencimiento = models.DateTimeField()
	terminada = models.BooleanField(default = False)