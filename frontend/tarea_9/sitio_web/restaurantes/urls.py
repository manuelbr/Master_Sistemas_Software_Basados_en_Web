# restaurantes/urls.py

from django.conf.urls import url
from django.conf.urls import include
from .views import IndexView
from rest_framework_mongoengine import routers
from . import views
from . import serializers

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'restaurants', serializers.restaurantsViewSet, r"restaurants")

urlpatterns = [
  url(r'^api/', include(router.urls, namespace='api')),
  url(r'^$', views.principal, name='index'),
  url(r'^principal', views.principal, name='principal'),
  #url(r'^muestraTexto', views.muestraTexto, name='muestraTexto'),
  #url(r'^muestraImagen', views.muestraImagen, name='muestraImagen'),
  url(r'^listar', views.listar, name='listar'),
  url(r'^busqueda', views.busqueda, name='busqueda'),
  url(r'^muestraResultado', views.muestraResultado, name='muestraResultado'),
  url(r'^insertar', views.insertar, name='insertar'),
  url(r'^restaurante/(?P<name>.+)/$', views.res_details, name='res_details'),

]
