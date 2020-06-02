from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_clasificacion(request):
	return HttpResponse("holaass clasificacion")
