##Clase 1

* __name__ establece el nombre del objeto en python que representa el script donde se coloca.
Es decir, si el script se llama pepito.py, el módulo se llamará pepito, y al importarlo se usará
ese nombre.
* Para concatenar scripts se usa el '+'.
* A parte del uso de la función 'make_response', una respuesta se puede crear desde cero a mano
importando el módulo Response y haciendo: 'respuesta = Response()'.
* Si importamos el modulo request podemos obtener los parámetros que pasamos por url (?param1=3), obteniéndolo con request.args.get('param1').
* El mecanismo de sesiones se hace con el módulo 'session', que utiliza persistencia y cookies para almacenar los usuarios que han hecho login.
* La notación de jinjer es sólo para utilizar variables, bucles y bloques que las utilicen. No es necesario incluirlas en los templates.
* En herencia, se usa {% block content %} {% endcontent %} para establecer que el trozo de código que hay entre esas dos partes se reutilizará, y usamos {% extends 'nombre.html' %} en el html hijo para decir que vas a utilizar el código que se ha especificado en el padre que puede heredarse. Por ejemplo si en el padre se ha puesto {%  %}
* Se usa url_for dentro de los href o imagenes dentro de las plantillas html para poder invocar contenido estático del directorio que le especifiquemos con el url_for. 
