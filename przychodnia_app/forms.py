from django import forms
from .models import Lekarz, Pacjent, Lek, Recepta


class DodajLekarza(forms.ModelForm):
    class Meta:
        model = Lekarz
        fields = '__all__'


class DodajPacjenta(forms.ModelForm):
    class Meta:
        model = Pacjent
        fields = '__all__'


class DodajLek(forms.ModelForm):
    class Meta:
        model = Lek
        fields = '__all__'


class DodajRecepte(forms.ModelForm):
    class Meta:
        model = Recepta
        fields = '__all__'
