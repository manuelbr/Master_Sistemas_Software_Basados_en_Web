# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from mongoengine import *
from lxml import etree
import sys, re
from models import *

#Especifico utf8 como el sistema de codificación por defecto
#(Para evitar problemas con acentos y demás...)
reload(sys)
sys.setdefaultencoding('utf8')

#Conecto con la base de datos de mongo (previamente cargada)
connect('test', host='localhost', port=27017)

#Página índice por defecto
@csrf_exempt
def login(request):
    if 'user' in request.session:
        #Si ya hay una sesión iniciada, se redirige a la página principal para que se le de la bienvenida
        return principal(request=request,user=request.session['user'])
    elif request.method == 'POST':
        #Si se reciben los datos de email desde un login anterior, se envian a la página principal y además se registra en la sesión
        request.session['user'] = request.POST.get('user')
        return principal(request=request,user=request.POST.get('user'))
    else:
        context = {}
        return render(request,'login.html',context)

#Página principal que da la bienvenida al usuario
def principal(request,user):
    context = {
        'user' : user,
    }
    return render(request,'principal.html',context)

#Página que muestra un texto y hereda de la principal
def muestraTexto(request):
    context = {
        'user' : request.session['user'],
        'titulo' : 'Esto es un titulo',
        'contenido' : 'Esto es una línea de texto plano',
    }
    return render(request,'muestraTexto.html',context)

#Página que muestra una imagen y hereda de la principal
def muestraImagen(request):
    context = {
        'user' : request.session['user'],
        'titulo' : 'Titulo de la imagen',

    }
    return render(request,'muestraImagen.html',context)

#Se deslogea al usuario de la sesión en la que se encuentra
def logout(request):
    request.session.pop('user', None)
    return redirect('/restaurantes')

#Página que muestra el formulario de búsqueda avanzada.
def busqueda(request):
    context = {
        'user' : request.session['user'],
    }
    return render(request,'busqueda.html',context)

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
                resultado = restaurants.objects(cuisine=re.compile(cuisine, re.IGNORECASE), address={'city':re.compile(locality, re.IGNORECASE)})
            elif name == "" and cuisine == "" and locality != "":
                resultado = restaurants.objects(address={'city':re.compile(locality, re.IGNORECASE)})
            elif name == "" and cuisine == "" and locality == "":
                resultado = restaurants.objects
            elif name == "" and cuisine != "" and locality == "":
                resultado = restaurants.objects(cuisine=re.compile(cuisine, re.IGNORECASE))
            elif name != "" and cuisine != "" and locality != "":
                resultado = restaurants.objects(name=re.compile(name, re.IGNORECASE),cuisine=re.compile(cuisine, re.IGNORECASE), address={'city':re.compile(locality, re.IGNORECASE)})
            elif name != "" and cuisine == "" and locality == "":
                resultado = restaurants.objects(name=re.compile(name, re.IGNORECASE))
            elif name != "" and cuisine != "" and locality == "":
                resultado = restaurants.objects(name = re.compile(name, re.IGNORECASE),cuisine=re.compile(cuisine, re.IGNORECASE))
            elif name != "" and cuisine == "" and locality != "":
                resultado = restaurants.objects(name = re.compile(name, re.IGNORECASE),address={'city':re.compile(locality, re.IGNORECASE)})
        else:
            resultado = restaurants.objects(name=re.compile(term, re.IGNORECASE))

        for r in resultado:
            lista.append(r)

        context = {
            'user' : request.session['user'],
            'lista': lista,
        }
        return render(request,'muestraResultado.html',context)

#Página que lista los 10 primeros restaurantes de la base de datos en mongo.
def listar(request):
    lista = []

    #Datos de los restaurantes a insertar
    restaurantes = ['Los Frutales','El Patio Andaluz','Bar Almudena','Bar Chorrohumo']
    localidades = ['Ogíjares','La Zubia','El Zaidín', 'Alhendín']
    str_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='
    sentinel = 0

    #Inserción de los restaurantes
    for rest in restaurantes:
        r = str_url + rest.replace(" ","+") +"+"+localidades[sentinel].replace(" ","+")
        tree = etree.parse(r)
        zipcode = tree.xpath('//address_component[type = "postal_code"]/long_name/text()')
        street = tree.xpath('//address_component[type = "route"]/long_name/text()')
        number = tree.xpath('//address_component[type = "street_number"]/long_name/text()')
        city = tree.xpath('//address_component[type = "administrative_area_level_2"]/long_name/text()')
        lat = tree.xpath('//location/lat/text()')
        lon = tree.xpath('//location/lng/text()')

        dir = Direccion(street=street[0]+", "+number[0], city=city[0],zipcode=int(zipcode[0]), coord=[float(lat[0]),float(lon[0])])  # así están bien
        r = restaurants(name=rest, cuisine="Granaina", borough=localidades[sentinel], address=dir)
        r.save()
        sentinel = sentinel + 1

    #Listado de los cuatro primeros restaurantes, los que hemos introducido
    for res in restaurants.objects.order_by('restaurant_id')[:4]:
        lista.append(res)

    context = {
        'user' : request.session['user'],
        'titulo' : 'Listado',
        'content' : lista,
        'muestraResultado': 'si',
    }
    return render(request,'listar.html',context)
