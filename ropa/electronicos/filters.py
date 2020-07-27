from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .models import categoria,ubicacion,electronico

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = electronico.objects.filter(usuario=request.user)
    electronico_contiene = request.GET.get('nombreelectronico')
    categoria_exacto = request.GET.get('categoriaelectronico')
    ubicacion_exacto = request.GET.get('ubicacionelectronico')


    if is_valid_queryparam(electronico_contiene):
        qs = qs.filter(nombre__icontains=electronico_contiene)

    if is_valid_queryparam(categoria_exacto) and categoria_exacto != 'Elige categoria...':
        qs = qs.filter(categoria__categoria=categoria_exacto)

    if is_valid_queryparam(ubicacion_exacto) and ubicacion_exacto != 'Elige ubicacion...':
        qs = qs.filter(ubicacion__ubicacion=ubicacion_exacto)
    
    return qs



