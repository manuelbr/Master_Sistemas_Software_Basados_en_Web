##Notas de la práctica 6
* La función is_valid() de django para objetos formularios, sirve para validar que los valores del formulario son correctos respecto a su definición.
* El formulario se establece como las clases de mongo, en el fichero de models.
* Con poner {% form %} en un template, se incluye el formulario en la página web. Justo encima debemos poner {% csrf_token %} para asegurar que se accede al formulario de forma segura en la misma máquina y no de forma externa.
* Se debe crear una página de creación de restaurantes (metiendo sus datos) y que incluya una foto del restaurante. En la función de buscar, cada nombre de cada restaurante será un enlace a una página que muestre la información detallada de cada restaurante: situación, tipo de comida, imagen, etc.
* En el url.py se debe definir que se accede a la información de cada restaurante con su id, en la misma url.
* (?P<year>[0-9]{4}) está en el url.py y se refiere a que la variable p, tendrá 4 números del 0 al 9.
* request.FILE['nombre del archivo'] obtenemos la imagen desde el formulario.
* Para subir archivos (la imagen) usamos <form enctype="multipart/form-data" ....>
* Para guardar la imagen, cuando haces read(), no puedes mandarlo directamente a la web, dado que sólo tienes un puntero a la base de datos. Habría que descargarla a partir de ese puntero y establecerlo donde queramos en el disco, y a partir de ahí incluirlo en la web.
* CharField() es lo que usa Django para los campos Stringfield de Mongo, y usa ImageField() también.
* El formulario de restaurantes tiene la misma estructura que una clase de Mongo que ya está metida.
* No se calculan los datos de los restaurantes por google, se meten todos a mano y ya está.
* Utilizar el formulario de bootstrap que ya se usa en la búsqueda.
* clase.image.put(request.FILES.get('foto')) para meter en el objeto de mongo la foto directamente (del disco a la bd en mongo).
Para escribir en disco la foto del objeto de mongo hacemos lo siguiente:
* with open('/tmp'+foto.name,'wb+') as destination:
    for chunk in foto.chunks():
        destination.write(chunk);

* {% form.as_p %} genera todo el contenido que debe haber dentro de un form (la cabecera del form debe ponerse si o sí en la plantilla de html), y entre medias debe estar este bloque, que define el formulario que necesitamos.
*   
