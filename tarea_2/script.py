#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response, send_file, request, session
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
@app.route('/',methods=['GET', 'POST'])
def login():
    if 'email' in session:
        #Si ya hay una sesión iniciada, se redirige a la página principal para que se le de la bienvenida
        return principal(email=session['email'])
    elif request.method == 'POST':
        #Si se reciben los datos de email desde un login anterior, se envian a la página principal y además se registra en la sesión
        session['email'] = request.form['email']
        return principal(email=request.form['email'])
    else:
        respuesta = make_response(render_template('login.html'))
        respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
        return respuesta

#Página principal que da la bienvenida al usuario
@app.route('/principal')
def principal(email):
    respuesta = make_response(render_template('principal.html',email=email))
    respuesta.headers['Content-Type'] = 'text/html; charset=utf-8'
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

    #Versión del profesor
    #usuarios = []
    #usuarios.append({'name':'Pepe','dni':'123456'})
    #usuarios.append({'name':'Paco','dni':'123456'})
    #usuarios.append({'name':'','dni':'123456'})
    #return render_template('hello.html',var='esto',usuarios=usuarios)

#Devuelve una imagen para visualizarla en el navegador
@app.route('/una_imagen')
def holaMundoImagen():
    filename = 'static/images/holaMundo.jpg'
    respuesta = make_response(send_file(filename))
    respuesta.headers['Content-Type'] = 'image/jpg'
    return respuesta

    #Forma alternativa del profesor
    #f = open(filename)
    #imagen = f.read()
    #f.close()
    #respuesta = make_response(imagen)
    #return respuesta

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

#Se utiliza para importar el módulo
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
