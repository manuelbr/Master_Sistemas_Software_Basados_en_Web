from __future__ import unicode_literals

from django import forms

class restaurantsForm(forms.Form):
    borough = forms.CharField()
    cuisine = forms.CharField()
    name = forms.CharField(required=True, max_length=80)
    restaurant_id = forms.IntegerField()
    building = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    zipcode = forms.IntegerField()
    imagen = forms.ImageField()
