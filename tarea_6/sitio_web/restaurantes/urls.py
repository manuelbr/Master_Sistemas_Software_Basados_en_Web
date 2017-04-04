# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.login, name='login'),
  url(r'^principal', views.principal, name='principal'),
  url(r'^muestraTexto', views.muestraTexto, name='muestraTexto'),
  url(r'^muestraImagen', views.muestraImagen, name='muestraImagen'),
  url(r'^logout', views.logout, name='logout'),
  url(r'^listar', views.listar, name='listar'),
  url(r'^busqueda', views.busqueda, name='busqueda'),
  url(r'^muestraResultado', views.muestraResultado, name='muestraResultado'),
  url(r'^insertar', views.insertar, name='insertar'),
]
