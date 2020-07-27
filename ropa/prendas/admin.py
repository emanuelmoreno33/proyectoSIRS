from django.contrib import admin

# Register your models here.
from .models import tipoprenda,tipocolor,tipomarca,prenda,playeracategoria,playeracorta,conjunto

class admintipo(admin.ModelAdmin):
    list_display=('id','tipo')
    list_filter=('id','tipo')

admin.site.register(tipoprenda,admintipo)

class admincolor(admin.ModelAdmin):
    list_display=('id','color','ejemplo')
    list_filter=('id','color','ejemplo')

admin.site.register(tipocolor,admincolor)

class adminmarca(admin.ModelAdmin):
    list_display=('id','marca')
    list_filter=('id','marca')

admin.site.register(tipomarca,adminmarca)

class adminprenda(admin.ModelAdmin):
    list_display=('nombre','tipo','marca','color','uso')
    list_filter=('nombre','tipo','marca','color','uso')

admin.site.register(prenda,adminprenda)

class admincategoria(admin.ModelAdmin):
    list_display=('id','categoria')
    list_filter=('id','categoria')

admin.site.register(playeracategoria,admincategoria)

class adminmangacorta(admin.ModelAdmin):
    list_display=('id','prenda','categoria')
    list_filter=('id','prenda','categoria')

admin.site.register(playeracorta,adminmangacorta)

class adminconjunto(admin.ModelAdmin):
    list_display=('id','nombre','descripcion')
    list_filter=('id','nombre','descripcion')
admin.site.register(conjunto,adminconjunto)