# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from mongoengine import *
from lxml import etree
from django.contrib.auth.decorators import login_required
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from django.views.generic.base import TemplateView
import time
import sys, re
import logging
from models import *
from forms import *

#Especifico utf8 como el sistema de codificación por defecto
#(Para evitar problemas con acentos y demás...)
reload(sys)
sys.setdefaultencoding('utf8')

#Obtengo una instancia del logger que usaré
logger = logging.getLogger(__name__)

#Página principal que da la bienvenida al usuario
@login_required
def principal(request):
    context = {}
    return render(request,'principal.html',context)

#Página que muestra un texto y hereda de la principal
def muestraTexto(request):
    context = {
        'titulo' : 'Esto es un titulo',
        'contenido' : 'Esto es una línea de texto plano',
    }
    logger.info(time.strftime("%H:%M:%S")+" se ha mostrado el texto")
    return render(request,'muestraTexto.html',context)

#Página que muestra una imagen y hereda de la principal
def muestraImagen(request):
    context = {
        'titulo' : 'Titulo de la imagen',
    }

    logger.info(time.strftime("%H:%M:%S")+" se ha mostrado la imagen")
    return render(request,'muestraImagen.html',context)

#Página que muestra el formulario de búsqueda avanzada.
def busqueda(request):
    context = {}
    logger.info(time.strftime("%H:%M:%S")+" se ha accedido al formulario de búsqueda")
    return render(request,'busqueda.html',context)

def handle_uploaded_file(f):
    with open('imagen', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def insertar(request):
    if request.method == 'POST':
        form = restaurantsForm(request.POST, request.FILES)
        if form.is_valid():
            borough = form.cleaned_data['borough']
            cuisine = form.cleaned_data['cuisine']
            name = form.cleaned_data['name']
            restaurant_id = form.cleaned_data['restaurant_id']
            building = form.cleaned_data['building']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            zipcode = form.cleaned_data['zipcode']
            imagen = request.FILES.get('imagen')

            res = restaurants(borough=borough,cuisine=cuisine,name=name,restaurant_id=(restaurants.objects.count() + 1),building=building,city=city,street=street,zipcode=zipcode)
            handle_uploaded_file(imagen)
            marmot = open('/home/manuelbr/Descargas/'+imagen.name, 'rb')
            res.imagen.put(marmot, content_type = imagen.content_type)
            res.save()

            form = restaurantsForm()
            context = {
                'titulo' : 'Insertar un restaurante',
                'form' : form,
            }
            logger.info(time.strftime("%H:%M:%S")+" se ha insertado un restaurante")
            return render(request,'insertar.html',context)
        else:
            context = {
                'form' : form,
            }
            return render(request,'insertar.html',context)
    else:
        form = restaurantsForm()
        context = {
            'titulo' : 'Insertar un restaurante',
            'form' : form,
        }
        return render(request,'insertar.html',context)

def res_details(request,name):

    resultado = restaurants.objects(name =  name.replace("+"," ")).first()

    context = {
        'restaurante' : name.replace("+"," "),
        'imagen' : resultado.imagen.read().encode("base64")
    }
    logger.info(time.strftime("%H:%M:%S")+" se ha accedido a los detalles de un restaurante")
    return render(request,'res_details.html',context)


#Página que realiza y muestra la búsqueda de un restaurante por su nombre.
def muestraResultado(request):
        term = request.GET.get('term')
        lista = []

        if term is None:
            name = request.GET.get('name')
            cuisine = request.GET.get('cuisine')
            locality = request.GET.get('locality')

            #Todas las posibilidades de rellenado del formulario
            if name == "" and cuisine != "" and locality != "":
                resultado = restaurants.objects(cuisine=re.compile(cuisine, re.IGNORECASE), city = re.compile(locality, re.IGNORECASE))
            elif name == "" and cuisine == "" and locality != "":
                resultado = restaurants.objects(city = re.compile(locality, re.IGNORECASE))
            elif name == "" and cuisine == "" and locality == "":
                resultado = restaurants.objects
            elif name == "" and cuisine != "" and locality == "":
                resultado = restaurants.objects(cuisine=re.compile(cuisine, re.IGNORECASE))
            elif name != "" and cuisine != "" and locality != "":
                resultado = restaurants.objects(name=re.compile(name, re.IGNORECASE),cuisine=re.compile(cuisine, re.IGNORECASE), city = re.compile(locality, re.IGNORECASE))
            elif name != "" and cuisine == "" and locality == "":
                resultado = restaurants.objects(name=re.compile(name, re.IGNORECASE))
            elif name != "" and cuisine != "" and locality == "":
                resultado = restaurants.objects(name = re.compile(name, re.IGNORECASE),cuisine=re.compile(cuisine, re.IGNORECASE))
            elif name != "" and cuisine == "" and locality != "":
                resultado = restaurants.objects(name = re.compile(name, re.IGNORECASE),city = re.compile(locality, re.IGNORECASE))
        else:
            resultado = restaurants.objects(name=re.compile(term, re.IGNORECASE))

        for r in resultado:
            lista.append(r)

        context = {
            'lista': lista,
        }
        logger.info(time.strftime("%H:%M:%S")+" se ha buscado un restaurante a través del formulario completo")
        return render(request,'muestraResultado.html',context)

#Página que lista los 10 primeros restaurantes de la base de datos en mongo.
def listar(request):
    lista = []

    #Listado de los cuatro primeros restaurantes, los que hemos introducido
    for res in restaurants.objects:
        lista.append(res)

    context = {
        'titulo' : 'Listado',
        'content' : lista,
        'muestraResultado': 'si',
    }
    logger.info(time.strftime("%H:%M:%S")+" se ha mostrado el listado de restaurantes")
    return render(request,'listar.html',context)


class IndexView(TemplateView):
    template_name = 'index.html'
