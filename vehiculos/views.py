from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from .models  import placa,garaje,auto
from django.urls import reverse_lazy
from django.views import generic
from .forms import Placaform, garajeform,autoform
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.db.models import Q
from .filters import filter,is_valid_queryparam

#placa
#delete
@method_decorator(login_required , name = "dispatch")
class placaDelete(generic.DeleteView):
	template_name = "transportes/deleteplaca.html"
	model = placa
	success_url = reverse_lazy("placalist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class placaUpdate(generic.UpdateView):
	template_name = "transportes/updateplaca.html"
	model = placa
	form_class = Placaform
	success_url = reverse_lazy("placalist")

#create
@method_decorator(login_required , name = "dispatch")
class placaCreate(generic.CreateView):
	template_name = "transportes/createplaca.html"
	model = placa
	form_class = Placaform
	success_url = reverse_lazy("placalist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(placaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def placalist(request):
	queryset = placa.objects.filter(usuario=request.user.id)
	context={
		"autos" : queryset
	}
	return render(request,"transportes/listplaca.html", context)

@login_required
def index(request):
	context={

	}
	return render(request,"transportes/index.html", context)


#garaje
#delete
@method_decorator(login_required , name = "dispatch")
class garajeDelete(generic.DeleteView):
	template_name = "transportes/deletegaraje.html"
	model = garaje
	success_url = reverse_lazy("garajelist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class garajeUpdate(generic.UpdateView):
	template_name = "transportes/updategaraje.html"
	model = garaje
	form_class = garajeform
	success_url = reverse_lazy("garajelist")

#create
@method_decorator(login_required , name = "dispatch")
class garajeCreate(generic.CreateView):
	template_name = "transportes/creategaraje.html"
	model = garaje
	form_class = garajeform
	success_url = reverse_lazy("garajelist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(garajeCreate, self).form_valid(form)

#list (por usuario)
@login_required
def garajelist(request):
	queryset = garaje.objects.filter(usuario=request.user.id)
	context={
		"autos" : queryset
	}
	return render(request,"transportes/listgaraje.html", context)


#autos
#create
@method_decorator(login_required , name = "dispatch")
class autoCreate(generic.CreateView):
	template_name = "transportes/create.html"
	model = auto
	form_class = autoform
	success_url = reverse_lazy("autolist")
	
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(autoCreate, self).form_valid(form)


#list (por usuario)
@login_required
def autolist(request):
	queryset = auto.objects.filter(usuario=request.user.id)
	context={
		"autos" : queryset
	}
	return render(request,"transportes/list.html", context)

#detail
@login_required
def autodetail(request,id):
	queryset = auto.objects.get(id=id)
	context={
	"object":queryset
}
	return render(request,"transportes/detail.html", context)


#UPDATE
@method_decorator(login_required , name = "dispatch")
class autoUpdate(generic.UpdateView):
	template_name = "transportes/update.html"
	model = auto
	form_class = autoform
	success_url = reverse_lazy("autolist")
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

#delete
@method_decorator(login_required , name = "dispatch")
class autoDelete(generic.DeleteView):
	template_name = "transportes/delete.html"
	model = auto
	success_url = reverse_lazy("autolist")


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'placa': placa.objects.filter(usuario=request.user),
        'garaje': garaje.objects.filter(usuario=request.user),
		'tipos': auto.tipo_elecciones,
		'marcas': auto.marca_elecciones

    }
    return render(request, "transportes/transporte_filter.html", context)