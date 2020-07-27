from django.urls import path,re_path
from django.conf import settings
from prendas import views
from django.conf.urls import url

urlpatterns = [
    path('deletecolor/<int:pk>',views.colorDelete.as_view(),name="colordelete"),
    path('updatecolor/<int:pk>',views.colorUpdate.as_view(), name="colorupdate"),
    path('createcolor/',views.colorCreate.as_view(),name="colorcreate"),
    path('listcolor/',views.colorlist,name="colorlist"),
   
   path('deletemarca/<int:pk>',views.marcaDelete.as_view(),name="marcadelete"),
    path('updatemarca/<int:pk>',views.marcaUpdate.as_view(), name="marcaupdate"),
    path('createmarca/',views.marcaCreate.as_view(),name="marcacreate"),
    path('listmarca/',views.marcalist,name="marcalist"),
    
    path('deletetipo/<int:pk>',views.tipoDelete.as_view(),name="tipodelete"),
    path('updatetipo/<int:pk>',views.tipoUpdate.as_view(), name="tipoupdate"),
    path('createtipo/',views.tipoCreate.as_view(),name="tipocreate"),
    path('listtipo/',views.tipolist,name="tipolist"),

    path('deletecategoria/<int:pk>',views.categoriaDelete.as_view(),name="categoriadelete"),
    path('updatecategoria/<int:pk>',views.categoriaUpdate.as_view(), name="categoriaupdate"),
    path('createcategoria/',views.categoriaCreate.as_view(),name="categoriacreate"),
    path('listcategoria/',views.categorialist,name="categorialist"),

    path('deleteprenda/<int:pk>',views.prendaDelete.as_view(),name="prendadelete"),
    path('updateprenda/<int:pk>',views.prendaUpdate.as_view(), name="prendaupdate"),
    path('detailprenda/<int:id>',views.prendadetail,name="prendadetail"),
    path('createprenda/',views.prendaCreate.as_view(),name="prendacreate"),
    path('listprenda/',views.prendalist,name="prendalist"),

    path('deletecorta/<int:pk>',views.cortaDelete.as_view(),name="cortadelete"),
    path('updatecorta/<int:pk>',views.cortaUpdate.as_view(), name="cortaupdate"),
    path('detailprenda/<int:id>',views.prendadetail,name="cortadetail"),
    path('createcorta/',views.cortaCreate.as_view(),name="cortacreate"),
    path('listcorta/',views.cortalist,name="cortalist"),

    path('deleteconjunto/<int:pk>',views.conjuntoDelete.as_view(),name="conjuntodelete"),
    path('updateconjunto/<int:pk>',views.conjuntoUpdate.as_view(), name="conjuntoupdate"),
    path('detailconjunto/<int:id>',views.conjuntodetail,name="conjuntodetail"),
    path('createconjunto/',views.conjuntoCreate.as_view(),name="conjuntocreate"),
    path('listconjunto/',views.conjuntolist,name="conjuntolist"),
    path('playeradeldia/',views.obtenerprendadia,name="deldia"),
    path('prendausada/<int:id>',views.prendausadas,name="prendausada"),
    
    path('',views.index,name="ropaindex"),
    path('lista1/', views.BootstrapFilterView,name="listafiltradaropa"),

]