from django import forms
from .models import placa,garaje,auto

class Placaform(forms.ModelForm):
	
	class Meta:
		model = placa
		fields=[
			"placa","descripcion"
		]

class garajeform(forms.ModelForm):
    class Meta:
        model= garaje
        fields=[
            "ubicacion"
        ]

class autoform(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(autoform, self).__init__(*args, **kwargs)
        self.fields['placa'].queryset =  placa.objects.filter(usuario=request.user)
        self.fields['garaje'].queryset =  garaje.objects.filter(usuario=request.user)
    class Meta:
        model= auto
        fields=[
            "modelo","marca","tipo","placa","garaje","imagen"
        ]

        labels={
            'modelo':'Nombre del automovil:',
            'marca':'Marca del automovil:',
            'tipo':'Tipo de automovil:',
            'placa':'Placa del automovil (opcional):',
            'garaje':'Garaje donde se encuentra:',
            'imagen':'Imagen del automovil (opcional):'
        }