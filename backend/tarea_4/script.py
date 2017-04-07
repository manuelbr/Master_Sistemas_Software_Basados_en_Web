##!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask import Flask, render_template, make_response, request, session, redirect, url_for
import sys
from mongoengine import *
from lxml import etree

#Especifico el nombre y la localización de la carpeta de recursos estáticos
app = Flask(__name__,static_url_path='')

#Activamos el modo de depuración para el tiempo de desarrollo
app.config['DEBUG'] = True

#Especifico la clave secreta para poder mantener sesiones de usuarios abiertas
app.secret_key = 'super secret key'

#Especifico utf8 como el sistema de codificación por defecto
#(Para evitar problemas con acentos y demás...)
reload(sys)
sys.setdefaultencoding('utf8')

#Conecto con la base de datos de mongo (previamente cargada)
connect('test', host='localhost', port=27017)

#Página índice por defecto
@app.route('/',methods=['GET', 'POST'])
def login():
    if 'user' in session:
        #Si ya hay una sesión iniciada, se redirige a la página principal para que se le de la bienvenida
        return principal(user=session['user'])
    elif request.method == 'POST':
        #Si se reciben los datos de email desde un login anterior, se envian a la página principal y además se registra en la sesión
        session['user'] = request.form['user']
        return principal(user=request.form['user'])
    else:
        respuesta = make_response(render_template('login.html'))
        respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
        return respuesta

#Página principal que da la bienvenida al usuario
@app.route('/principal')
def principal(user):
    respuesta = make_response(render_template('principal.html',user=user))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta

#Página que muestra un texto y hereda de la principal
@app.route('/muestraTexto')
def muestraTexto():
    respuesta = make_response(render_template('muestraTexto.html',user=session['user'],titulo='Esto es un título',contenido='Esto es una línea de texto plano'))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta

#Página que muestra una imagen y hereda de la principal
@app.route('/muestraImagen')
def muestraImagen():
    respuesta = make_response(render_template('muestraImagen.html',user=session['user'],titulo='Título de la Imagen'))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta

#Se deslogea al usuario de la sesión en la que se encuentra
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

#Se utiliza para importar el módulo
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

class Grados(EmbeddedDocument):
    date = DateTimeField()
    grade = StringField(max_length=1)
    score = IntField()

class Direccion(EmbeddedDocument):
    building = StringField()
    coord    = GeoPointField()
    city = StringField()
    street = StringField()
    zipcode = IntField()

#Se crea la arquitectura de los objetos tipo "Documento"
class restaurants(Document):
    address = EmbeddedDocumentField("Direccion")
    borough = StringField()
    cuisine = StringField()
    grades = ListField(EmbeddedDocumentField("Grados"))
    name = StringField(required=True, max_length=80)
    restaurant_id = IntField()

#Página que realiza y muestra la búsqueda de un restaurante por su nombre.
@app.route('/buscar',methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        respuesta = make_response(render_template('busqueda.html',user=session['user'],muestraResultado='no'))
        respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
        return respuesta
    else:
        restaurante = request.form['term']
        localidad = request.form['localidad']
        str_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='
        r = str_url + restaurante + localidad
        tree = etree.parse(r)
        dire = tree.xpath('//formatted_address/text()')
        lat = tree.xpath('//location/lat/text()')
        lon = tree.xpath('//location/lng/text()')

        if len(dire) != 0:
            respuesta = make_response(render_template('busqueda.html',user=session['user'],titulo='Resultado de la búsqueda',nombre=restaurante,dire=dire[0],lat=lat,lon=lon, muestraResultado='si'))
            respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
            return respuesta
        else:
            respuesta = make_response(render_template('busqueda.html',user=session['user'],titulo='Resultado de la búsqueda',error='No se ha encontrado el restaurante', muestraResultado='si'))
            respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
            return respuesta

#Página que lista los 10 primeros restaurantes de la base de datos en mongo.
@app.route('/listar')
def listar():
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
        localidad = tree.xpath('//address_component[type = "locality"]/long_name/text()')
        city = tree.xpath('//address_component[type = "administrative_area_level_2"]/long_name/text()')
        lat = tree.xpath('//location/lat/text()')
        lon = tree.xpath('//location/lng/text()')

        print(r)
        print("Zipcode "+zipcode[0])
        print("Calle "+street[0])
        print("Número "+number[0])
        print("Localidad "+localidad[0])
        print("Ciudad "+city[0])

        dir = Direccion(street=street[0]+", "+number[0], city=localidad[0]+", "+city[0],zipcode=int(zipcode[0]), coord=[float(lat[0]),float(lon[0])])  # así están bien
        r = restaurants(name=rest, cuisine="Granaina", borough=localidades[sentinel], address=dir)
        r.save()
        sentinel = sentinel + 1

    #Listado de los cuatro primeros restaurantes, los que hemos introducido
    for res in restaurants.objects.order_by('restaurant_id')[:4]:
        lista.append(res)
    respuesta = make_response(render_template('busqueda.html',user=session['user'],titulo='Resultado de la búsqueda',content=lista, muestraResultado='si'))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta
