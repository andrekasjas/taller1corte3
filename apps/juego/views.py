from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_juego(request):
	return HttpResponse("holaass juego")