from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from lxml import etree

class Grados(EmbeddedDocument):
    date = DateTimeField()
    grade = StringField(max_length=1)
    score = IntField()

class Direccion(EmbeddedDocument):
    building = StringField()
    coord    = GeoPointField()
    city = StringField()
    street = StringField()
    zipcode = IntField()

#Se crea la arquitectura de los objetos tipo "Documento"
class restaurants(Document):
    address = EmbeddedDocumentField("Direccion")
    borough = StringField()
    cuisine = StringField()
    grades = ListField(EmbeddedDocumentField("Grados"))
    name = StringField(required=True, max_length=80)
    restaurant_id = IntField()
