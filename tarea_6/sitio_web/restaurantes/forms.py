# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

class restaurantsForm(forms.Form):
    borough = forms.CharField(label='Barrio',required=False)
    cuisine = forms.CharField(label='Tipo de cocina',required=False)
    name = forms.CharField(label='Nombre del local',required=True, max_length=80)
    restaurant_id = forms.IntegerField(label='Id del restaurante')
    building = forms.CharField(label='Nombre de edificio (si procede)',required=False)
    city = forms.CharField(label='Ciudad de localización',required=False)
    street = forms.CharField(label='Calle',required=False)
    zipcode = forms.IntegerField(label='Código postal',required=False)
    imagen = forms.ImageField(label='Imagen del restaurante',required=False)
