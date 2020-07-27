from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class categoria (models.Model):
    categoria = models.CharField(max_length=50)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.categoria

class ubicacion (models.Model):
    ubicacion = models.CharField(max_length=50)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.ubicacion

class electronico(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)
    cantidad= models.IntegerField(validators=[MaxValueValidator(100000,'Debe ser menos de 100,000'),MinValueValidator(1,'Debe haber al menos 1')])
    disponible = models.IntegerField(validators=[MaxValueValidator(100000,'Debe ser menos de 100,000'),MinValueValidator(0,'Debe ser 0 o mayor')])
    descripcion = models.TextField(blank = True)
    costo = models.DecimalField(max_digits=9,decimal_places=2,validators=[MaxValueValidator(1000000,'Debe ser menor a 1,000,000'),MinValueValidator(0,'Debe ser 0 o mayor')])
    imagen = models.ImageField(blank = True)
    ubicacion = models.ForeignKey(ubicacion,on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

