from django.db import models

# Create your models here.

class Pais(models.Model):
	pai_id = models.IntegerField(primary_key=True)
	pai_nom = models.CharField(max_length=60)
	pai_des = models.CharField(max_length=250)

	def __str__(self):
		return '{}'.format(self.pai_nom)