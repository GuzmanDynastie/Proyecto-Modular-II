from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def imprimir(request):
    return HttpResponse("<h1>Hola mundo</h1>")

def acerca(request):
    return HttpResponse("About")