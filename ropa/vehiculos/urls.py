from django.urls import path
from django.conf import settings
from vehiculos import views

urlpatterns = [
    path('deleteplaca/<int:pk>',views.placaDelete.as_view(),name="placaDelete"),
    path('updateplaca/<int:pk>',views.placaUpdate.as_view(), name="placaUpdate"),
    path('createplaca/',views.placaCreate.as_view(),name="placaCreate"),
    path('listplaca/',views.placalist,name="placalist"),
    path('',views.index,name="vehiculosindex"),
    
    path('deletegaraje/<int:pk>',views.garajeDelete.as_view(),name="garajeDelete"),
    path('updategaraje/<int:pk>',views.garajeUpdate.as_view(), name="garajeUpdate"),
    path('creategaraje/',views.garajeCreate.as_view(),name="garajeCreate"),
    path('listgaraje/',views.garajelist,name="garajelist"),
    
    path('deleteauto/<int:pk>',views.autoDelete.as_view(),name="autoDelete"),
    path('updateauto/<int:pk>',views.autoUpdate.as_view(), name="autoUpdate"),
    path('detailauto/<int:id>',views.autodetail, name="autodetail"),
    path('createauto/',views.autoCreate.as_view(),name="autoCreate"),
    path('listauto/',views.autolist,name="autolist"),

    path('list1/',views.BootstrapFilterView,name="listafiltroauto"),

]