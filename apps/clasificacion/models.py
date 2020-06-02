from django.db import models

# Create your models here.

class Clasificacion(models.Model):
	cla_id = models.IntegerField(primary_key=True)
	cla_nom = models.CharField(max_length=60)
	cla_des = models.CharField(max_length=250)