from django import forms
from apps.pais.models import Pais

class PaisForm(forms.ModelForm):
	class Meta:
		model = Pais
		fields = [
			'pai_id',
			'pai_nom',
			'pai_des',
		]
		labels = {
			'pai_id':'Codigo postal del pais',
			'pai_nom':'Nombre del pais',
			'pai_des':'Descripcion del pais',	
		}
		widgets = {
			'pai_id': forms.TextInput(attrs={'class':'form-control'}),
			'pai_nom':forms.TextInput(attrs={'class':'form-control'}),
			'pai_des':forms.TextInput(attrs={'class':'form-control'}),
		}