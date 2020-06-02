from django import forms
from apps.desarrollador.models import Desarrollador

class DesarrolladorForm(forms.ModelForm):
	class Meta:
		model = Desarrollador
		fields =[
			'des_id',
			'des_nom',
			'des_ape',
			'des_tel',
			'des_email', 
			'des_pai_id',
		]
		labels={
			'des_id':'Cedula del desarrollador',
			'des_nom':'Nombre del desarrollador',
			'des_ape':'Apellido del desarrollador',
			'des_tel':'Telefono del desarrollador',
			'des_email':'Correo del desarrollador', 
			'des_pai_id':'Pais del desarrollador',	
		}
		widgets={
		    'des_id': forms.TextInput(attrs={'class':'form-control'}),
			'des_nom': forms.TextInput(attrs={'class':'form-control'}),
			'des_ape': forms.TextInput(attrs={'class':'form-control'}),
			'des_tel': forms.TextInput(attrs={'class':'form-control'}),
			'des_email': forms.TextInput(attrs={'class':'form-control'}), 
			'des_pai_id': forms.Select(attrs={'class':'form-control'}),
		}