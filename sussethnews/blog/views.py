from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#MVT
#Model
#view
#Template
#Importacion de Librerias Personales
from . import models


def listar_noticias(request):
	"""
		Obtiene las noticias de la base de datos 

		Retorna:
			El listado de las noticias
	"""
	#Obtiene el listado de todas las noticia 
	#De las base de datos y la asigna a la variable
	#noticias
	noticias = models.Noticia.objects.all() 

	#Retorna todo renderizado para ser leido en el 
	#explorador, tiene tres parametros
	#Solicitud(request), plantilla de datos y datos
	return render(
					request, 
					"./noticias/index.html",
					{"news":noticias}
				)

def ver_noticia(request, id_noticia):
	"""
		Obtiene una noticia de la base de datos

		Parametros:
			id_noticia es numerico y hace referencia
			al identificador de la noticia buscada

		Retorna
			La noticia buscada si existe
	"""

	noticia = models.Noticia.objects.get(id=id_noticia)

	return render(
					request,
					"./noticias/detalle.html",
					{"noticia":noticia}
				)