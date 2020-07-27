from django.db import models
from django.conf import settings

class placa(models.Model):
	placa = models.CharField(max_length=8)
	descripcion = models.TextField(blank = True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	def __str__(self):
		return self.placa

class garaje(models.Model):
	ubicacion = models.CharField(max_length=100)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	def __str__(self):
		return self.ubicacion

class auto(models.Model):
	tipo_elecciones=[
		('Motocicleta','Motocicleta'),
		('Deportivos','Deportivos'),
		('Compactos','Compactos'),
		('Cupés','Cupés'),
		('Emergencias','Emergencias'),
		('Industriales','Industriales'),
		('Militares','Militares'),
		('Todoterrenos','Todoterrenos'),
		('Muscle','Muscle'),
		('Sedanes','Sedanes'),
		('Servicio','Servicio'),
		('Deportivo clasicos','Deportivo clásicos'),
		('Súper','Súper'),
		('Todocaminos','Todocaminos'),
		('Especializados','Especializados'),
		('Furgonetas','Furgonetas'),
		('Ruedas descubiertas','Ruedas descubiertas')

	]
	marca_elecciones=[
		('Nagasaki','Nagasaki'),
		('Shitzu','Shitzu'),
		('Dinka','Dinka'),
		('Vapid','Vapid'),
		('Albany','Albany'),
		('Invetero','Invetero'),
		('Imponte','Imponte'),
		('Bravado','Bravado'),
		('Cheval','Cheval'),
		('Declasse','Declasse'),
		('Enus','Enus'),
		('Dewbauchee','Dewbauchee'),
		('Lampadati','Lampadati'),
		('Ocelot','Ocelot'),
		('Ubermacht','Ubermacht'),
		('HVY','HVY'),
		('Jobuilt','Jobuilt'),
		('Maibatsu','Maibatsu'),
		('MTL','MTL'),
		('Brute','Brute'),
		('Dinka','Dinka'),
		('Karin','Karin'),
		('Weeny','Weeny'),
		('Benefactor','Benefactor'),
		('Bollokan','Bollokan'),
		('Obey','Obey'),
		('Grotti','Grotti'),
		('Pifster','Pifster'),
		('Annis','Annis'),
		('Schyster','Schyster'),
		('Hijak','Hijak'),
		('Pegassi','Pegassi'),
		('Truffade','Truffade'),
		('Western','Western'),
		('Stanley','Stanley'),
		('Zirconium','Zirconium'),
		('LCC','LCC'),
		('Principe','Principe'),
		('Gallivanter','Gallivanter'),
		('Fathom','Fathom'),
		('Emperor','Emperor'),
		('Dundreary','Dundreary'),
		('Mammoth','Mammoth'),
		('Canis','Canis'),
		('BF','BF'),
		('Coil','Coil'),
		('Vulcar','Vulcar'),
		('Överflöd','Överflöd'),
		('Progen','Progen'),
		('Willard','Willard'),
		('Maxwell','Maxwell'),
		('Vysser','Vysser'),
		('Vom Feuer','Vom Feuer'),
		('Desconocido','Desconocido'),
	]
	modelo = models.CharField(max_length = 50)
	marca = models.CharField(max_length=100,choices=marca_elecciones)
	tipo = models.CharField(max_length=100,choices=tipo_elecciones)
	placa = models.ForeignKey(placa, on_delete=models.CASCADE, blank=True,null=True)
	garaje=models.ForeignKey(garaje, on_delete=models.CASCADE)
	imagen = models.ImageField(blank = True)
	fecha_registro = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	def __str__(self):
		return self.modelo
