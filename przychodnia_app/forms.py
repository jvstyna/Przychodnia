from django import forms
from .models import Lekarz, Pacjent, Lek, Recepta


class DodajLekarza(forms.ModelForm):
    class Meta:
        model = Lekarz
        fields = ('imie_nazwisko', 'numer_telefonu', 'email', 'specjalizacja')

        widgets = {
            'imie_nazwisko': forms.TextInput(attrs={'class': 'form-control'}),
            'numer_telefonu': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'specjalizacja': forms.Select(attrs={'class': 'form-control'})
        }


class DodajPacjenta(forms.ModelForm):
    class Meta:
        model = Pacjent
        fields = ('imie_nazwisko', 'numer_telefonu', 'email', 'plec', 'data_urodzenia', 'pesel')

        widgets = {
            'imie_nazwisko': forms.TextInput(attrs={'class': 'form-control'}),
            'numer_telefonu': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'plec': forms.Select(attrs={'class': 'form-control'}),
            'data_urodzenia': forms.SelectDateWidget(years=range(1900, 2022), attrs={'class': 'form-control'}),
            'pesel': forms.NumberInput(attrs={'class': 'form-control'})
        }


class DodajLek(forms.ModelForm):
    class Meta:
        model = Lek
        fields = ('nazwa', 'substancja_czynna', 'cena')

        widgets = {
            'nazwa': forms.TextInput(attrs={'class': 'form-control'}),
            'substancja_czynna': forms.TextInput(attrs={'class': 'form-control'}),
            'cena': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DodajRecepte(forms.ModelForm):
    class Meta:
        model = Recepta
        fields = '__all__'
        fields = ('pacjent', 'lekarz', 'lek', 'data', 'zalecenie')

        widgets = {
            'pacjent': forms.Select(attrs={'class': 'form-control'}),
            'lekarz': forms.Select(attrs={'class': 'form-control'}),
            'lek': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'zalecenie': forms.Textarea(attrs={'class': 'form-control'})
        }
