#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, send_file
import sys

#Especifico el nombre y la localización de la carpeta de recursos estáticos
app = Flask(__name__,static_url_path='/home/manuelbr/Dropbox/Sistemas Software Basados en Web/tarea_1/Static')

#Activamos el modo de depuración para el tiempo de desarrollo
app.config['DEBUG'] = True

#Especifico utf8 como el sistema de codificación por defecto
#(Para evitar problemas con acentos y demás...)
reload(sys)
sys.setdefaultencoding('utf8')

#Página índice por defecto
@app.route('/')
def index():
    respuesta = make_response('Hola, esta es la página índice')
    respuesta.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return respuesta

#Devuelve un texto plano
@app.route('/un_texto_plano')
def holaMundo():
    respuesta = make_response('Esto es un texto plano cualquiera')
    respuesta.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return respuesta

#Devuelve el template html que hay en la carpeta 'templates'
@app.route('/contenido_html')
def holaMundoHtml():
    respuesta = make_response(render_template('hello.html'))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta

#Devuelve una imagen para visualizarla en el navegador
@app.route('/una_imagen')
def holaMundoImagen():
    filename = 'static/images/holaMundo.jpg'
    respuesta = make_response(send_file(filename))
    respuesta.headers['Content-Type'] = 'image/jpg'
    return respuesta

#Devuelve en texto plano aquello que escribimos a partir de 'este_texto_plano'
@app.route('/este_texto_plano/<parametro>')
def returnParametro(parametro):
    respuesta = make_response('El parámetro que se ha pasado es: %s' % parametro)
    respuesta.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return respuesta

#Página de error
@app.errorhandler(404)
def page_not_found(e):
    respuesta = make_response(render_template('error.html'), 404)
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
    return respuesta
