from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola esta es una nueva aplicación de django')

