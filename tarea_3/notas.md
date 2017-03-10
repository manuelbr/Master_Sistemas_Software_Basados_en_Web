##Notas de la práctica 4
###Geolocalización con Google
* Hay que instalar la librería request con pip, que realiza peticiones a direcciones y devuelven los resultados. Los resultados vienen en xml o en json. Hay que pedirlos con el enlace que dice que los resultados sean en json (para hacerlo todo en json).
* Se hace una petición a la api de google para geolocalización y se recibe todo en json.
* import json para incluir json. a = json.loads() y luego b = a['results']['address_components'] y luego hacemos c = b[6] para sacar el código postal y luego d = c['long_name'] para el código postal.
* Las peticiones a la api se hacen personalizadas en función de los restaurantes que vamos metiendo, para obtener su geolocalización.
* r = request.get('url') para hacer las peticiones desde python con el paquete request. r.text para obtener el texto de la respuesta.
