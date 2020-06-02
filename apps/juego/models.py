from django.db import models
from apps.desarrollador.models import Desarrollador
from apps.clasificacion.models import Clasificacion

# Create your models here.

class Juego(models.Model):
	jue_id = models.IntegerField(primary_key=True)
	jue_nom = models.CharField(max_length=60)
	jue_val = models.IntegerField()
	jue_des = models.CharField(max_length=250)
	jue_des_id = models.ForeignKey(Desarrollador, null=True, blank=True, on_delete=models.CASCADE)
	jue_cla_id = models.ForeignKey(Clasificacion, null=True, blank=True, on_delete=models.CASCADE)