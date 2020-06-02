from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.pais.forms import PaisForm
from apps.pais.models import Pais
# Create your views here.

def index(request):
	return render(request,'pais/index.html')

def pais_view(request):
	if request.method == 'POST':
		form = PaisForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(index)
	else:
		form = PaisForm()

	return render(request,'pais/pais_form.html',{'form':form})

def pais_list(request):
	pais = Pais.objects.all().order_by('pai_nom')
	contexto = {'paises':pais}
	return render(request,'pais/pais_list.html',contexto) 

def pais_edit(request,id_pais):
	pais = Pais.objects.get(pai_id=id_pais)
	if request.method == 'GET':
		form = PaisForm(instance=pais)
	else:
		form = PaisForm(request.POST, instance=pais)
		if form.is_valid():
			form.save()
		return redirect(pais_list)
	return render(request, 'pais/pais_form.html', {'form':form})

def pais_delete(request, id_pais):
	pais = Pais.objects.get(pai_id=id_pais)
	if request.method == 'POST':
		pais.delete()
		return redirect(pais_list)
	return render(request, 'pais/pais_delete.html', {'pais':pais})