from django.db import models
from .models import *

# Create your models here.

class Lluvia(models.Model):
    fecha_registro = models.DateField()
    probabilidad_lluvia = models.FloatField()
    precipitaciones = models.FloatField()
    fecha_pronostico = models.DateField()
    
    @property
    def esperanza_lluvia(self):
        return self.probabilidad_lluvia*self.precipitaciones

    