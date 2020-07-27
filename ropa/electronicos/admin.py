from django.contrib import admin
from .models import categoria,ubicacion,electronico
# Register your models here.

class admincategoria(admin.ModelAdmin):
    list_display=('id','categoria')
    list_filter=('id','categoria')

admin.site.register(categoria,admincategoria)

class adminubicacion(admin.ModelAdmin):
    list_display=('id','ubicacion')
    list_filter=('id','ubicacion')

admin.site.register(ubicacion,adminubicacion)

class adminelectronico(admin.ModelAdmin):
    list_display=('id','nombre','categoria','cantidad','ubicacion')
    list_filter=('id','nombre','categoria','cantidad','ubicacion')

admin.site.register(electronico,adminelectronico)
