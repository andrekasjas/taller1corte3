from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.desarrollador.forms import DesarrolladorForm
from apps.desarrollador.models import Desarrollador
# Create your views here.

def index_desarrollador(request):
	return render(request,'desarrollador/index.html')

def desarrollador_view(request):
	if request.method == 'POST':
		form = DesarrolladorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(index_desarrollador)
	else:
		form = DesarrolladorForm()

	return render(request,'desarrollador/desarrollador_form.html',{'form':form})

def desarrollador_list(request):
	desarrollador = Desarrollador.objects.all()
	contexto = {'desarrolladores':desarrollador}
	return render(request,'desarrollador/desarrollador_list.html',contexto) 