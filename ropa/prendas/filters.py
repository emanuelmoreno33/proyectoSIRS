from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .models import tipoprenda,tipocolor,tipomarca,playeracategoria,prenda,playeracorta,conjunto

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = prenda.objects.filter(usuario=request.user)
    prenda_contiene = request.GET.get('nombreprenda')
    tipo_exacto = request.GET.get('tipoprenda')
    color_exacto = request.GET.get('colorprenda')
    marca_exacto = request.GET.get('marcaprenda')
    prenda_uso = request.GET.get('usado')
    prenda_nouso = request.GET.get('nousado')


    if is_valid_queryparam(prenda_contiene):
        qs = qs.filter(nombre__icontains=prenda_contiene)

    if is_valid_queryparam(tipo_exacto) and tipo_exacto != 'Elige tipo...':
        qs = qs.filter(tipo__tipo=tipo_exacto)

    if is_valid_queryparam(color_exacto) and tipo_exacto != 'Elige color...':
        qs = qs.filter(color__color=color_exacto)

    if is_valid_queryparam(marca_exacto) and marca_exacto != 'Elige marca...':
        qs = qs.filter(marca__marca=marca_exacto)

    if prenda_uso == 'on':
        qs = qs.filter(uso=True)

    elif prenda_nouso == 'on':
        qs = qs.filter(uso=False)
    
    return qs



