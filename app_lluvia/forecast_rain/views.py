from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from .models import Lluvia
from django.core import serializers
import json
# Create your views here.


def index(request):
    return HttpResponse('Hola esta es una nueva aplicación de django')


def forecast(request):
    driver = webdriver.Firefox(
        executable_path=r'C:\Users\calve\Documents\Portafolio\Lluvia\lluvia\app_lluvia\utils\geckodriver.exe')
        
    fecha = []
    probabilidad = []
    precipitaciones = []
    fecha_pronostico = []
    esperanza_lluvia = []
    acumulado = []

    for dia in range(1, 91):
        # Scraper
        values = scrapper_rain(driver, dia)

        # Add values
        fecha.append(values['fecha'])
        probabilidad.append(values['probabilidad'])
        precipitaciones.append(values['precipitaciones'])
        fecha_pronostico.append(values['fecha_pronostico'])
        esperanza_lluvia.append(values['esperanza_lluvia'])
        acumulado.append(sum(esperanza_lluvia))

        #Save in database
        lluvia = Lluvia.objects.create(
            fecha_registro=values['fecha'],
            probabilidad_lluvia=values['probabilidad'],
            precipitaciones=values['precipitaciones'],
            fecha_pronostico=values['fecha_pronostico'])

    data = {'fecha': fecha, 'probabilidad': probabilidad, 'precipitaciones': precipitaciones, 'fecha_pronostico': fecha_pronostico,
            'acumulado': acumulado}

    return JsonResponse(data)


def scrapper_rain(driver, dia):
    fecha = date.today()
    driver.get(
        f"https://www.accuweather.com/es/cl/santiago/60449/daily-weather-forecast/60449?day={dia}")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    tabla = soup.find_all('p', {'class': 'panel-item'})
    for i in tabla:
        value = i.get_text(separator=",").split(",")
        if value[0] == "Probabilidad de precipitación":
            probabilidad = float(value[1].replace("%", ""))/100
        if value[0] == "Precipitaciones":
            precipitaciones = float(value[1].replace("mm", ""))
            break
    fecha_pronostico = fecha+timedelta(days=(dia-1))
    esperanza_lluvia = probabilidad*precipitaciones
    values = {'fecha': fecha, 'probabilidad': probabilidad, 'precipitaciones': precipitaciones, 'fecha_pronostico': fecha_pronostico,
              'esperanza_lluvia': esperanza_lluvia}
    return values

def forecast_data(request):
    SomeLluvia_json = serializers.serialize("json", Lluvia.objects.all())
    data = json.loads(SomeLluvia_json)
    return JsonResponse(data,safe=False)

def graph(request):
    return render(request, 'forecast_rain/graph.html')