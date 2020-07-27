from django import forms
from .models import categoria,ubicacion,electronico

class categoriaform(forms.ModelForm):
    class Meta:
        model = categoria
        fields =[
            "categoria"
        ]

class ubicacionform(forms.ModelForm):
    class Meta:
        model = ubicacion
        fields =[
            "ubicacion"
        ]

class electronicoform(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(electronicoform, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset =  categoria.objects.filter(usuario=request.user)
        self.fields['ubicacion'].queryset =  ubicacion.objects.filter(usuario=request.user)
    class Meta:
        model = electronico
        fields =[
            "nombre","categoria","cantidad","disponible","descripcion","costo","imagen","ubicacion"
        ]