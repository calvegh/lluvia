from django.contrib import admin
from .models import *
# Register your models here.


class LluviaAdmin(admin.ModelAdmin):
	list_display = ('fecha_registro', 'probabilidad_lluvia', 'precipitaciones', 'fecha_pronostico','esperanza_lluvia')

admin.site.register(Lluvia, LluviaAdmin)