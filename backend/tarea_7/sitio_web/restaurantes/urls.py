# restaurantes/urls.py

from django.conf.urls import url
from django.conf.urls import include
from .views import IndexView

from . import views

urlpatterns = [
  url(r'^$', views.principal, name='index'),
  url(r'^principal', views.principal, name='principal'),
  url(r'^muestraTexto', views.muestraTexto, name='muestraTexto'),
  url(r'^muestraImagen', views.muestraImagen, name='muestraImagen'),
  url(r'^listar', views.listar, name='listar'),
  url(r'^busqueda', views.busqueda, name='busqueda'),
  url(r'^muestraResultado', views.muestraResultado, name='muestraResultado'),
  url(r'^insertar', views.insertar, name='insertar'),
  url(r'^(?P<resid>\d+)/$', views.res_details, name='res_details'),
  #url(r'^accounts/login', include('registration.backends.simple.urls')),
]
