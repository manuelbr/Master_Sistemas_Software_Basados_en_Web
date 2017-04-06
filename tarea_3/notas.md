## Notas de la práctica 4
* Hay que instalar la librería request con pip, que realiza peticiones a direcciones y devuelven los resultados. Los resultados vienen en xml o en json. Hay que pedirlos con el enlace que dice que los resultados sean en json (para hacerlo todo en json).
* Se hace una petición a la api de google para geolocalización y se recibe todo en json.
* import json para incluir json. a = json.loads() y luego b = a['results']['address_components'] y luego hacemos c = b[6] para sacar el código postal y luego d = c['long_name'] para el código postal.
* Las peticiones a la api se hacen personalizadas en función de los restaurantes que vamos metiendo, para obtener su geolocalización.
* r = request.get('url') para hacer las peticiones desde python con el paquete request. r.text para obtener el texto de la respuesta.
* Si lo hacemos con xml, para obtenerlo ordenado de cara a utilizarlo con xpath, primero tenemos que crear un árbol con las etiquetas.
* En Xpath, si ponemos //autor, sacamos el valor de la etiqueta autor, sea donde sea que esté, porque si no lo ponemos hay que representar donde está en función de toda la arquitectura del árbol de etiquetas al que pertenece.
* La latitud y longitud de la localización de los bares de granada está al revés en los resultados que devuelve google.
* tree.xpath('long_name/text()')[6] para obtener por xpath el codigo postal de la geolocalización del resultado de la api de google con xml. Antes de usar la variable tree, tienes que inicializarla así:  
