from django.urls import path
from django.conf import settings
from electronicos import views

urlpatterns = [
    path('',views.index,name="coleccionindex"),

    path('deletecategoria/<int:pk>',views.categoriaDelete.as_view(),name="categoriadelete2"),
    path('updatecategoria/<int:pk>',views.categoriaUpdate.as_view(), name="categoriaupdate2"),
    path('createcategoria/',views.categoriaCreate.as_view(),name="categoriacreate2"),
    path('listcategoria/',views.categorialist,name="categorialist2"),

    path('deleteubicacion/<int:pk>',views.ubicacionDelete.as_view(),name="ubicaciondelete"),
    path('updateubicacion/<int:pk>',views.ubicacionUpdate.as_view(), name="ubicacionupdate"),
    path('createubicacion/',views.ubicacionCreate.as_view(),name="ubicacioncreate"),
    path('listubicacion/',views.ubicacionlist,name="ubicacionlist"),

    path('deletecoleccion/<int:pk>',views.electronicoDelete.as_view(),name="electronicodelete"),
    path('updatecoleccion/<int:pk>',views.electronicoUpdate.as_view(), name="electronicoupdate"),
    path('detailcoleccion/<int:id>',views.electronicodetail,name="electronicodetail"),
    path('createcoleccion/',views.electronicoCreate.as_view(),name="electronicocreate"),
    path('listcoleccion/',views.electronicolist,name="electronicolist"),

    path('list1/',views.BootstrapFilterView,name="listafiltroelectronico"),
    
]