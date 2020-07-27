from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from .models import tipoprenda,tipocolor,tipomarca,playeracategoria,prenda,playeracorta,conjunto
from django.urls import reverse_lazy
from django.views import generic
from .forms import tipo,color,marca,categoria,prendaform,playcortaform,conjuntoform
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.db.models import Q
import random
from django.db.models import Max
from .filters import filter,is_valid_queryparam
# Create your views here.

@login_required
def index(request):
	context={

	}
	return render(request,"prendas/index.html", context)

#color
#create
@method_decorator(login_required , name = "dispatch")
class colorCreate(generic.CreateView):
	template_name = "prendas/createcolor.html"
	model = tipocolor
	form_class = color
	success_url = reverse_lazy("colorlist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(colorCreate, self).form_valid(form)

#list (por usuario)
@login_required
def colorlist(request):
	queryset = tipocolor.objects.filter(usuario=request.user.id)
	context={
		"color" : queryset
	}
	return render(request,"prendas/listcolor.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class colorDelete(generic.DeleteView):
	template_name = "prendas/deletecolor.html"
	model = tipocolor
	success_url = reverse_lazy("colorlist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class colorUpdate(generic.UpdateView):
	template_name = "prendas/updatecolor.html"
	model = tipocolor
	form_class = color
	success_url = reverse_lazy("colorlist")


#marcas
#create
@method_decorator(login_required , name = "dispatch")
class marcaCreate(generic.CreateView):
	template_name = "prendas/createmarca.html"
	model = tipomarca
	form_class = marca
	success_url = reverse_lazy("marcalist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(marcaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def marcalist(request):
	queryset = tipomarca.objects.filter(usuario=request.user.id)
	context={
		"marca" : queryset
	}
	return render(request,"prendas/listmarca.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class marcaDelete(generic.DeleteView):
	template_name = "prendas/deletemarca.html"
	model = tipomarca
	success_url = reverse_lazy("marcalist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class marcaUpdate(generic.UpdateView):
	template_name = "prendas/updatemarca.html"
	model = tipomarca
	form_class = marca
	success_url = reverse_lazy("marcalist")

#tipo de prenda
#create
@method_decorator(login_required , name = "dispatch")
class tipoCreate(generic.CreateView):
	template_name = "prendas/createtipo.html"
	model = tipoprenda
	form_class = tipo
	success_url = reverse_lazy("tipolist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(tipoCreate, self).form_valid(form)

#list (por usuario)
@login_required
def tipolist(request):
	queryset = tipoprenda.objects.filter(usuario=request.user.id)
	context={
		"tipo" : queryset
	}
	return render(request,"prendas/listtipo.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class tipoDelete(generic.DeleteView):
	template_name = "prendas/deletetipo.html"
	model = tipoprenda
	success_url = reverse_lazy("tipolist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class tipoUpdate(generic.UpdateView):
	template_name = "prendas/updatetipo.html"
	model = tipoprenda
	form_class = tipo
	success_url = reverse_lazy("tipolist")

#categoria de la manga corta
#create
@method_decorator(login_required , name = "dispatch")
class categoriaCreate(generic.CreateView):
	template_name = "prendas/createcorta.html"
	model = playeracategoria
	form_class = categoria
	success_url = reverse_lazy("categorialist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(categoriaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def categorialist(request):
	queryset = playeracategoria.objects.filter(usuario=request.user.id)
	context={
		"categoria" : queryset
	}
	return render(request,"prendas/listcategoria.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class categoriaDelete(generic.DeleteView):
	template_name = "prendas/deletecategoria.html"
	model = playeracategoria
	success_url = reverse_lazy("categorialist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class categoriaUpdate(generic.UpdateView):
	template_name = "prendas/updatecorta.html"
	model = playeracategoria
	form_class = categoria
	success_url = reverse_lazy("categorialist")

#prenda
#create
@method_decorator(login_required , name = "dispatch")
class prendaCreate(generic.CreateView):
	template_name = "prendas/create.html"
	model = prenda
	form_class = prendaform
	success_url = reverse_lazy("prendalist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(prendaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def prendalist(request):
	queryset = prenda.objects.filter(usuario=request.user.id)
	context={
		"categoria" : queryset
	}
	return render(request,"prendas/list.html", context)

#detail
@login_required
def prendadetail(request,id):
	queryset = prenda.objects.get(id=id)
	context={
	"object":queryset
}
	return render(request,"prendas/detail.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class prendaDelete(generic.DeleteView):
	template_name = "prendas/delete.html"
	model = prenda
	success_url = reverse_lazy("prendalist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class prendaUpdate(generic.UpdateView):
	template_name = "prendas/update.html"
	model = prenda
	form_class = prendaform
	success_url = reverse_lazy("prendalist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

#manga corta
#create
@method_decorator(login_required , name = "dispatch")
class cortaCreate(generic.CreateView):
	template_name = "prendas/createcorta.html"
	model = playeracorta
	form_class = playcortaform
	success_url = reverse_lazy("cortalist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(cortaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def cortalist(request):
	queryset = playeracorta.objects.filter(prenda__usuario=request.user.id)
	context={
		"categoria" : queryset
	}
	return render(request,"prendas/listcorta.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class cortaDelete(generic.DeleteView):
	template_name = "prendas/deletecorta.html"
	model = playeracorta
	success_url = reverse_lazy("cortalist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class cortaUpdate(generic.UpdateView):
	template_name = "prendas/updatecorta.html"
	model = playeracorta
	form_class = playcortaform
	success_url = reverse_lazy("cortalist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

#conjuntos
#create
@method_decorator(login_required , name = "dispatch")
class conjuntoCreate(generic.CreateView):
	template_name = "prendas/createconjunto.html"
	model = conjunto
	form_class = conjuntoform
	success_url = reverse_lazy("conjuntolist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(conjuntoCreate, self).form_valid(form)

#list (por usuario)
@login_required
def conjuntolist(request):
	queryset = conjunto.objects.filter(usuario=request.user.id)
	context={
		"conjunto" : queryset
	}
	return render(request,"prendas/listconjunto.html", context)

#detail
@login_required
def conjuntodetail(request,id):
	queryset = conjunto.objects.get(id=id)
	context={
	"object":queryset
}
	return render(request,"prendas/detailconjunto.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class conjuntoDelete(generic.DeleteView):
	template_name = "prendas/deleteconjunto.html"
	model = conjunto
	success_url = reverse_lazy("conjuntolist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class conjuntoUpdate(generic.UpdateView):
	template_name = "prendas/updateconjunto.html"
	model = conjunto
	form_class = conjuntoform
	success_url = reverse_lazy("conjuntolist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs


@login_required
def obtenerprendadia(request):
	conteo = playeracorta.objects.filter(usada=False,prenda__usuario=request.user.id).count()
	queryset = playeracorta.objects.filter(usada=False,prenda__usuario=request.user.id)
	if conteo > 0:
		randoms = random.choice(queryset)
	else:
		randoms = "ninguno"
	context={
	"object":randoms
}
	return render(request,"prendas/detaildeldia.html", context)

@login_required
def prendausadas(request,id):
	play = playeracorta.objects.get(id=id)
	play.usada = True
	play.save()
	return redirect('/closet/listcorta')


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'tipo': tipoprenda.objects.filter(usuario=request.user),
        'color': tipocolor.objects.filter(usuario=request.user),
        'marca': tipomarca.objects.filter(usuario=request.user),

    }
    return render(request, "prendas/prenda_filter.html", context)