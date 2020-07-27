from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from general import views
from django.contrib.auth.views import logout_then_login

urlpatterns=[
    path('',views.index,name="login"),
    path('cerrar/',logout_then_login, name="logout"),
    path('signup/',views.signup.as_view(),name="signup"),
    path('prendalist/',views.PrendaListAPIView.as_view(),name="APIprenda"),
    path('playeralist/',views.PlayeracortaListAPIView.as_view(),name="APIplayera"),
    path('conjuntolist/',views.ConjuntoListAPIView.as_view(),name="APIconjunto"),
    path('electronicolist/',views.ElectronicosListAPIView.as_view(),name="APIelectronico"),
    path('vehiculolist/',views.VehiculosListAPIView.as_view(),name="APIvehiculo")
]