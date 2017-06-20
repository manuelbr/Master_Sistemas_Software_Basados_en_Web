## Notas de tarea 1 frontend
* En la aplicación que tenemos, hay que resaltar las opciones del menú cuando pasemos el ratón por encima.
* También podemos crear una pantalla emergente (un modal) que salte con determinado evento (con AJAX).
* En Jquery, si ponemos $( 'a' ).click(function( event ){ codigo }), ese 'a' se refiere al tipo de enlace de html y css. Siempre podemos tratar con los tipos de datos de html. Por ejemplo $( '#id' ) ó ( '.clase' ). Esto se usa para añadir eventos a los elementos del tipo que especificamos.
* Para poner que la función que ejecutamos sólo lo haga cuando la página esté cargada del todo (porque jquery es asíncrono como javascript a veces), hay que poner $( document ).ready(function(){}).
* También podemos modificar el css y el html sobre la marcha. $( 'h1' ).css({ contenido css }). Lo mismo se hace para html pero con la etiqueta html.
* Lo que hay que hacer e modificar el css en tiempo de ejecución con jquery para que cuando pasemos el ratón por encima de una de las pestañas del menú, se resalte. También se puede usar la opción class=active que ya tenía por tener bootstrap. Podríamos cambiar el html en tiempo de ejecución para añadir y quitar esa clase en función de lo que queramos.
* Poner también un evento que cuando pase el ratón por un determinado sitio que se haga un console.log('') (la consola que se abre es la del navegador, que hay que abrirla a propósito), un alert que avise que se ha producido el evento con jquery. O bien que cuando pasemos el ratón por el menú, se ponga rojo.
* $( "#identificador" ).addClass({Añadimos la clase active a ese identificador}). El identificador debería provenir de la plantilla, al cambiar de pestaña.
* Con ajax puedes hacer que salga una pantalla emergente de algún enlace, conectándose con el servidor y ofreciendo información. Por ejemplo, que cuando pasemos el ratón por el enlace de un restaurante en la lista de enlaces que se muestre en esa ventana emergente el mapa de google maps. Esto se llama modal. Hay que sacar el modal con jquery (jquery.show). En bootstrap puedes obtener los modales como quieras.
* Para poner que salga el modal podemos poner: $( '#id' ).modal().
