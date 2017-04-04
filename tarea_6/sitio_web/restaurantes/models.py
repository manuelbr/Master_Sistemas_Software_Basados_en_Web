from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from lxml import etree

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
