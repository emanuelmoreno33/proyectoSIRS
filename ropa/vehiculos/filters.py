from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .models import placa,garaje,auto

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = auto.objects.filter(usuario=request.user)
    modelo_contiene = request.GET.get('nombreauto')
    marca_exacto = request.GET.get('marcaauto')
    tipo_exacto = request.GET.get('tipoauto')
    placa_exacto = request.GET.get('placaauto')
    garaje_exacto = request.GET.get('garajeauto')


    if is_valid_queryparam(modelo_contiene):
        qs = qs.filter(modelo__icontains=modelo_contiene)

    if is_valid_queryparam(marca_exacto) and marca_exacto != 'Elige marca...':
        qs = qs.filter(marca=marca_exacto)

    if is_valid_queryparam(tipo_exacto) and tipo_exacto != 'Elige tipo...':
        qs = qs.filter(marca=tipo_exacto)

    if is_valid_queryparam(placa_exacto) and placa_exacto != 'Elige placa...':
        qs = qs.filter(placa__placa=placa_exacto)
    
    if is_valid_queryparam(garaje_exacto) and garaje_exacto != 'Elige garaje...':
        qs = qs.filter(garaje__ubicacion=garaje_exacto)
    
    return qs


