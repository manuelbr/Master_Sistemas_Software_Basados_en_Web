##!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask import Flask, render_template, make_response, request, session, redirect, url_for
import sys
from mongoengine import *

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
        termino = request.form['term']
        lista = []
        #collection = db['restaurants']
        #print(collection.,file=sys.stderr)
        for res in restaurants:
            print(po.name,file=sys.stderr)
            lista.append(po.name)
        respuesta = make_response(render_template('busqueda.html',user=session['user'],titulo='Resultado de la búsqueda',content=lista, muestraResultado='si'))
        respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
        return respuesta

#Página que lista todos los restaurantes por su nombre.
@app.route('/listar')
def listar():
    lista = []
    for res in restaurants.objects[:3]:
        lista.append(res.name)
    respuesta = make_response(render_template('busqueda.html',user=session['user'],titulo='Resultado de la búsqueda',content=lista, muestraResultado='si'))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta
