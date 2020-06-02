from django.db import models
from apps.pais.models import Pais

# Create your models here.


class Desarrollador(models.Model):
	des_id = models.IntegerField(primary_key=True)
	des_nom = models.CharField(max_length=60)
	des_ape = models.CharField(max_length=60)
	des_tel = models.CharField(max_length=60)
	des_email = models.CharField(max_length=90)
	des_pai_id = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.des_pai_id)


