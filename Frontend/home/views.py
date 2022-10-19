from django.http import HttpResponse
from django.shortcuts import render
from .services import Configuraciones
"""
def hello(request):
    return HttpResponse("Hello word")"""
def index(request):
    return render(request,"index.html")

def loadSettings(request):
    return render(request, "configuracion.html")

def loadSettingsMessages(request):
    return render(request, "consumidos.html")

def viewData(request):
    return render(request, "views.html")


