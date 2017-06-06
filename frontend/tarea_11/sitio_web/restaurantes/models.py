from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from lxml import etree

#Conecto con la base de datos de mongo (previamente cargada)
connect('restaurantes', host='database', port=27017)

#Se crea la arquitectura de los objetos tipo "Documento"
class restaurants(Document):
    borough = StringField()
    cuisine = StringField()
    name = StringField(required=True, max_length=80)
    restaurant_id = IntField()
    building = StringField()
    city = StringField()
    street = StringField()
    zipcode = IntField()
    imagen = ImageField()
