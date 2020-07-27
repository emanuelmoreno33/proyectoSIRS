from django import forms
from .models import tipoprenda,tipocolor,tipomarca,playeracategoria,prenda,playeracorta,conjunto
from fractions import Fraction
from camera_imagefield import CameraImageField


class tipo (forms.ModelForm):
    class Meta:
        model = tipoprenda
        fields=[
            "tipo"
        ]

class color (forms.ModelForm):
    class Meta:
        model = tipocolor
        fields =[
            "color","ejemplo"
        ]

class marca (forms.ModelForm):
    class Meta:
        model = tipomarca
        fields = [
            "marca"
        ]

class categoria (forms.ModelForm):
    class Meta:
        model = playeracategoria
        fields=[
            "categoria"
        ]

class prendaform (forms.ModelForm):
    
    def __init__(self, request, *args, **kwargs):
        super(prendaform, self).__init__(*args, **kwargs)
        self.fields['tipo'].queryset =  tipoprenda.objects.filter(usuario=request.user)
        self.fields['marca'].queryset =  tipomarca.objects.filter(usuario=request.user)
        self.fields['color'].queryset =  tipocolor.objects.filter(usuario=request.user)
    class Meta:
        imagen = CameraImageField(aspect_ratio=Fraction(16, 9))
        model = prenda
        fields = [
            "nombre","tipo","marca","color","imagen","notas","cantidad","uso"
        ]
        widget ={
            "imagen" : CameraImageField(aspect_ratio=Fraction(16, 9))
        }

class playcortaform (forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(playcortaform, self).__init__(*args, **kwargs)
        self.fields['prenda'].queryset =  prenda.objects.filter(usuario=request.user)
        self.fields['categoria'].queryset =  playeracategoria.objects.filter(usuario=request.user)
    class Meta:
        model = playeracorta
        fields = [
            "prenda","categoria","usada"
        ]


class conjuntoform (forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(conjuntoform, self).__init__(*args, **kwargs)
        self.fields['prendas'].queryset =  prenda.objects.filter(usuario=request.user)
    class Meta:
        model = conjunto
        fields = [
            "nombre","descripcion","prendas"
        ]
