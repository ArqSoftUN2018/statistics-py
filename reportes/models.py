from django.db import models

class Reporte(models.Model):
	descripcion = models.CharField(max_length = 100)