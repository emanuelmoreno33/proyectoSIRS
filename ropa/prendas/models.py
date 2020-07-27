from django.db import models
from django.conf import settings
from spectrum.fields import ColorField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class tipoprenda(models.Model):
    tipo = models.CharField(max_length=50)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.tipo

class tipocolor (models.Model):
    color = models.CharField(max_length=50)
    ejemplo = ColorField(_('color'), default='#FFFF00')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.color

class tipomarca (models.Model):
    marca = models.CharField(max_length=50)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.marca

class playeracategoria(models.Model):
    categoria = models.CharField(max_length=50)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.categoria

class prenda(models.Model):
    nombre = models.CharField(max_length=50)
    tipo=models.ForeignKey(tipoprenda, on_delete=models.CASCADE)
    marca=models.ForeignKey(tipomarca, on_delete=models.CASCADE)
    color = models.ForeignKey(tipocolor,on_delete=models.CASCADE)
    imagen = models.ImageField(blank = True)
    fecha_registro = models.DateField(auto_now_add=True)
    notas = models.TextField(blank= True)
    cantidad = models.IntegerField(validators=[MaxValueValidator(100000,'Debe ser menor de 100,000'),MinValueValidator(1,'Debe haber al menos 1')])
    uso = models.BooleanField(default=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class playeracorta(models.Model):
    prenda = models.OneToOneField(prenda,on_delete=models.CASCADE)
    categoria = models.ForeignKey(playeracategoria,on_delete=models.CASCADE)
    usada = models.BooleanField(default=False)
    def __str__(self):
        return self.prenda.nombre

class conjunto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    prendas = models.ManyToManyField(prenda)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre