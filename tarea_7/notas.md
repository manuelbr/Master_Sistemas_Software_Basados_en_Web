##Notas de la práctica 7
* Se basa en la inclusión de autenticación y registro dentro la aplicación web.
* Vamos a usar dos bases de datos, la mysql que es interna del django: el usuario, para lo cual django tiene un objeto determinado con tablas ya creadas y por otro lado mongodb con todo lo incluido anteriormente.
* El objeto de django para registrar usuarios se llama user.
* Poniendo @login_required antes de una función, si no se está autentificado se nos lleva a la página de login, cuando se logea, ya sí ejecuta la función.
* User está dentro de request, por lo que podemos acceder a él desde las plantillas.
* Hay que instalar un paquete de django que gracias a él la página de logeo y todo lo relacionado con él se hace solo. La página de login original ya no nos sirve de nada.
* Hay que seguir el tutorial que viene en la tarea para poder realizarlo.
* Hay que crear una carpeta que se llame registration dentro de templates y meter dentro todas las plantillas de la pantalla de logeo.
* Por último añadiremos un sistema de log que recoja todas las acciones que se realizan, almacenando la información en una base de datos. Para ello usaremos la libreria de logs de pyhton. Dentro de lo que es el proceso de log, se debe especificar el tipo de mensaje que envia: warning, alert, etc. Para cada mensaje puede definirse un actuador que: lo envíe a un archivo, lo envíe por correo, etc. Los logs deben ir a un archivo que los reuna.
* {% if user.is_authenticated %} {% else %} {% endif %}
*  Cuando pones logger.debug('%s  ha hehco una busqueda de: %s', )
