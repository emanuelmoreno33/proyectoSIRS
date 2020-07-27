from rest_framework import serializers
from django.contrib.auth.models import User
from prendas.models import prenda,playeracorta,conjunto,tipoprenda,tipocolor,tipomarca,playeracategoria
from electronicos.models import categoria,ubicacion,electronico
from vehiculos.models import placa,garaje,auto

#prendas
class tipoprendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoprenda
        fields = ['tipo']

class tipocolorSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipocolor
        fields = ['color','ejemplo']

class TipomarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipomarca
        fields = ['marca']

class PlayeracategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = playeracategoria
        fields = ['categoria']

class PrendaSerializer(serializers.ModelSerializer):
    tipo = tipoprendaSerializer(read_only=True)
    color = tipocolorSerializer(read_only=True)
    marca = TipomarcaSerializer(read_only=True)
    class Meta:
        model = prenda
        fields = ['id',
        'nombre',
        'tipo',
        'marca',
        'color',
        'imagen',
        'notas',
        'cantidad'
		]

class PlayeracortaSerializer(serializers.ModelSerializer):
    prenda = PrendaSerializer(read_only=True)
    categoria = PlayeracategoriaSerializer(read_only=True)
    class Meta:
        model = playeracorta
        fields =['id',
        'prenda',
        'categoria'
        ]

class ConjuntoSerializer (serializers.ModelSerializer):
    prendas = PrendaSerializer(read_only=True,many=True)
    class Meta:
        model = conjunto
        fields = ['id',
        'nombre',
        'descripcion',
        'prendas',
        ]

#electronicos
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'categoria'
        ]

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'ubicacion'
        ]

class ElectronicoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    ubicacion = UbicacionSerializer(read_only=True)
    class Meta:
        fields = [
            'id',
            'nombre',
            'categoria',
            'cantidad',
            'disponible',
            'descripcion',
            'costo',
            'imagen',
            'ubicacion',
        ]

#vehiculos
class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'placa',
            'descripcion'
        ]

class GarajeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'ubicacion'
        ]

class AutoSerializer(serializers.ModelSerializer):
    placa = PlacaSerializer(read_only=True)
    garaje = GarajeSerializer(read_only=True)
    class Meta:
        fields = [
            'id',
            'modelo',
            'marca',
            'tipo',
            'placa',
            'garaje',
            'imagen',
            'fecha_registro'
        ]

