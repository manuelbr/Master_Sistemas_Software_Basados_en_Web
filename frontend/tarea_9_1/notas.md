## Notas de la tarea 9_1 (REST + AUTENTICACIÓN)

Consiste en añadir el proceso de autenticación a la api de la tarea 8. Para ello se siguen los siguientes pasos:

* curl -X POST -d "username=USER&password=PASS" http://localhost:8000/restaurantes/obtain-auth-token/ , para obtener el token de autenticación para un usuario concreto.
* curl -H "Authorization: Token token" localhost:8000/restaurantes/api/restaurants/
