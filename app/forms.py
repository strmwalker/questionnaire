from django import forms

from app.models import Color, Animal


class NameForm(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()


class LookForm(forms.Form):
    profile_photo = forms.ImageField()
    hair_color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.Select, to_field_name='name')
    weight = forms.IntegerField()


class AnimalForm(forms.Form):
    favorite_animal = forms.ModelChoiceField(queryset=Animal.objects.all(), widget=forms.Select, to_field_name='name')
    has_pet = forms.ChoiceField(choices=((True, 'yes'), (False, 'no')))
