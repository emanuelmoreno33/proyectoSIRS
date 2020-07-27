from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views import generic
from django.urls import reverse_lazy
from .forms import loginForm,Users_form
from .serializers import tipoprendaSerializer,tipocolorSerializer,TipomarcaSerializer,PlayeracategoriaSerializer,PrendaSerializer,PlayeracortaSerializer,ConjuntoSerializer,CategoriaSerializer,UbicacionSerializer,ElectronicoSerializer,PlacaSerializer,GarajeSerializer,AutoSerializer
from electronicos.forms import categoria,ubicacion,electronico
from prendas.forms import tipoprenda,tipocolor,tipomarca,playeracategoria,prenda,playeracorta,conjunto
from vehiculos.forms import placa,garaje,auto
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions


# Create your views here.

class signup(generic.FormView):
	template_name='general/signup.html'
	form_class =Users_form
	success_url = reverse_lazy('login')

	def form_valid(self,form):
		user = form.save()
		return super(signup,self).form_valid(form)


# Create your views here.
def index(request):
	message = "Inicia sesion para continuar"
	form = loginForm(request.POST or None)
	if request.method == "POST":
		form = loginForm(request.POST or None)
		if form.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username =username,password =password)
			if user is not None:
				if user.is_active:
					login(request,user)
					message = "user logged"
				else:
					message = "user is not active"
			else:
				message = "Username or password is not correct"
		context={
			"nombre":"Emanuel",
			"message":message,
			"form":form
			}
	context={
	"form":form,
	"message":message
	}
	return render(request,"general/index.html",context)


class PrendaListAPIView(generics.ListAPIView):
    serializer_class = PrendaSerializer
    queryset = prenda

    def get_queryset(self,*args,**kargs):
    	return prenda.objects.filter(usuario = self.request.user)

class PlayeracortaListAPIView(generics.ListAPIView):
	serializer_class = PlayeracortaSerializer
	queryset = playeracorta

	def get_queryset(self,*args,**kargs):
		return playeracorta.objects.filter(prenda__usuario = self.request.user)

class ConjuntoListAPIView(generics.ListAPIView):
	serializer_class = ConjuntoSerializer
	queryset = conjunto

	def get_queryset(self,*args,**kargs):
		return conjunto.objects.filter(usuario=self.request.user)

class ElectronicosListAPIView(generics.ListAPIView):
	serializer_class = ElectronicoSerializer
	queryset = electronico

	def get_queryset(self,*args,**kargs):
		return electronico.objects.filter(usuario=self.request.user)

class VehiculosListAPIView(generics.ListAPIView):
	serializer_class = AutoSerializer
	queryset = auto

	def get_queryset(self,*args,**kargs):
		return auto.objects.filter(usuario=self.request.user)
