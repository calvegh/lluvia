from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('forecast',views.forecast, name='forecast'),
    path('graph',views.graph,name='graph'),
    path('forecast_data',views.forecast_data, name='forecast_data')
]