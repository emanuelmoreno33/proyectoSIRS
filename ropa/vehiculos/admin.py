from django.contrib import admin
from .models import placa,garaje,auto
# Register your models here.

class adminplaca(admin.ModelAdmin):
    list_display=('id','placa','descripcion')
    list_filter=('id','placa','descripcion')

admin.site.register(placa,adminplaca)

class admingaraje(admin.ModelAdmin):
    list_display=('id','ubicacion')
    list_filter=('id','ubicacion')

admin.site.register(garaje,admingaraje)

class adminauto(admin.ModelAdmin):
    list_display=('id','modelo','marca','tipo','garaje','imagen')
    list_filter=('id','modelo','marca','tipo','garaje','imagen')

admin.site.register(auto,adminauto)