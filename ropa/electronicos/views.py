from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from .models import categoria,ubicacion,electronico
from django.urls import reverse_lazy
from django.views import generic
from .forms import categoriaform,ubicacionform,electronicoform
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.db.models import Q
from .filters import filter,is_valid_queryparam

# Create your views here.


@login_required
def index(request):
	context={

	}
	return render(request,"electronicos/index.html", context)

#categoria
#create
@method_decorator(login_required , name = "dispatch")
class categoriaCreate(generic.CreateView):
	template_name = "electronicos/createcategoria.html"
	model = categoria
	form_class = categoriaform
	success_url = reverse_lazy("categorialist2")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(categoriaCreate, self).form_valid(form)

#list (por usuario)
@login_required
def categorialist(request):
	queryset = categoria.objects.filter(usuario=request.user.id)
	context={
		"categoria" : queryset
	}
	return render(request,"electronicos/listcategoria.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class categoriaDelete(generic.DeleteView):
	template_name = "electronicos/deletecategoria.html"
	model = categoria
	success_url = reverse_lazy("categorialist2")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class categoriaUpdate(generic.UpdateView):
	template_name = "electronicos/updatecategoria.html"
	model = categoria
	form_class = categoriaform
	success_url = reverse_lazy("categorialist2")



#ubicacion
#create
@method_decorator(login_required , name = "dispatch")
class ubicacionCreate(generic.CreateView):
	template_name = "electronicos/createubicacion.html"
	model = ubicacion
	form_class = ubicacionform
	success_url = reverse_lazy("ubicacionlist")

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(ubicacionCreate, self).form_valid(form)

#list (por usuario)
@login_required
def ubicacionlist(request):
	queryset = ubicacion.objects.filter(usuario=request.user.id)
	context={
		"ubicacion" : queryset
	}
	return render(request,"electronicos/listubicacion.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class ubicacionDelete(generic.DeleteView):
	template_name = "electronicos/deleteubicacion.html"
	model = ubicacion
	success_url = reverse_lazy("ubicacionlist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class ubicacionUpdate(generic.UpdateView):
	template_name = "electronicos/updateubicacion.html"
	model = ubicacion
	form_class = ubicacionform
	success_url = reverse_lazy("ubicacionlist")

#electronico
#create
@method_decorator(login_required , name = "dispatch")
class electronicoCreate(generic.CreateView):
	template_name = "electronicos/create.html"
	model = electronico
	form_class = electronicoform
	success_url = reverse_lazy("electronicolist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def  form_valid(self,form):
		form.instance.usuario = self.request.user
		form.save()
		return super(electronicoCreate, self).form_valid(form)

#list (por usuario)
@login_required
def electronicolist(request):
	queryset = electronico.objects.filter(usuario=request.user.id)
	context={
		"electronico" : queryset
	}
	return render(request,"electronicos/list.html", context)

#detail
@login_required
def electronicodetail(request,id):
	queryset = electronico.objects.get(id=id)
	context={
	"object":queryset
}
	return render(request,"electronicos/detail.html", context)

#delete
@method_decorator(login_required , name = "dispatch")
class electronicoDelete(generic.DeleteView):
	template_name = "electronicos/delete.html"
	model = electronico
	success_url = reverse_lazy("electronicolist")

#UPDATE
@method_decorator(login_required , name = "dispatch")
class electronicoUpdate(generic.UpdateView):
	template_name = "electronicos/update.html"
	model = electronico
	form_class = electronicoform
	success_url = reverse_lazy("electronicolist")

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'categoria': categoria.objects.filter(usuario=request.user),
        'ubicacion': ubicacion.objects.filter(usuario=request.user),

    }
    return render(request, "electronicos/electronico_filter.html", context)