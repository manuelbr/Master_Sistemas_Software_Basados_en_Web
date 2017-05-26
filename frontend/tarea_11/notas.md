## Notas de la tarea 11 (Despliegue de la app)

Consiste en añadir en poner en fase de producción la web y desplegarla usando docker/docker-compose. Para ejecutar el servidor wsgi con gunicorn:

* gunicorn sitio_web.wsgi

El token de autorización se le pasa a la api de forma directa con el usuario del administrador, ya que no hay tiempo para obtener la contraseña del usuario (y no estoy seguro de que sea muy bueno conseguir esos datos).
