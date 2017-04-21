## Notas de la tarea 9 (REST)

* El views.py y los templates no van a hacer falta, ya que se usará la libreria onepage, que usa Ajax para cargar dinámicamente desde el servidor.
* Ya no funcionará con urls la prágina, sino con una api que hará llamadas a datos específicos, no a páginas completas. La api estará en el navegador y por tanto, el servidor quedará mucho más descargado de trabajo que de otra forma.
* Priorizar el uso de URIs con estructura de directorios y evitar el paso de variables. https://api/restaurantes/Bar_Pepe en vez de https://api/restaurantes/?name=Bar_Pepe.
* No hay que usar el codigo del views, ya que la api lo hace todo sola.
* Lo que hay que hacer es instalar la api que se dice en el guión de prácticas (one page) y hacer que esa api haga las funciones de CRUD, que ya tiene implementadas: Leer, escribir, actualizar y eliminar restaurantes.
* Ahora, todo el código de creación de restaurantes y subida de imagenes ya no sería necesario, dado que lo hace la api sola.
* Para trasladar al móvil el uso de la web con la api, se usará React de javascript: una serie de librerias. Es algo parecido a Angular. Hay que seguir los tutoriales que hay en swad.
* La parte de react se hará la semana que viene. Esta centrarse en la parte de la API.
