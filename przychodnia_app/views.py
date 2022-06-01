from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DodajLek, DodajLekarza, DodajRecepte, DodajPacjenta
from .models import Pacjent, Lekarz, Lek, Recepta
import csv
import datetime


def index(request):
    return render(request, 'index.html')


def dodaj_lek(request):
    if request.method == 'GET':
        form = DodajLek()
    if request.method == 'POST':
        form = DodajLek(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #dodaj htmla tutaj z widokiem wyboru kolejnej aktywnosci

    return render(request, 'dodaj_lek.html', {
        'form': form
    })


def dodaj_lekarza(request):
    if request.method == 'GET':
        form = DodajLekarza()
    if request.method == 'POST':
        form = DodajLekarza(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #dodaj htmla tutaj z widokiem wyboru kolejnej aktywnosci

    return render(request, 'dodaj_lekarza.html', {
        'form': form
    })


def dodaj_recepte(request):
    if request.method == 'GET':
        form = DodajRecepte()
    if request.method == 'POST':
        form = DodajRecepte(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #dodaj htmla tutaj z widokiem wyboru kolejnej aktywnosci

    return render(request, 'dodaj_recepte.html', {
        'form': form
    })


def dodaj_pacjenta(request):
    if request.method == 'GET':
        form = DodajPacjenta()
    if request.method == 'POST':
        form = DodajPacjenta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #dodaj htmla tutaj z widokiem wyboru kolejnej aktywnosci

    return render(request, 'dodaj_pacjenta.html', {
        'form': form
    })


def wyswietl_lek(request):
    leki = Lek.objects.all()
    return render(request, 'wyswietl_lek.html', {
        'leki': leki
    })


def wyswietl_recepte(request):
    recepty = Recepta.objects.all()
    return render(request, 'wyswietl_recepte.html', {
        'recepty': recepty
    })


def wyswietl_pacjenta(request):
    pacjenci = Pacjent.objects.all()
    return render(request, 'wyswietl_pacjenta.html', {
        'pacjenci': pacjenci
    })


def wyswietl_lekarza(request):
    lekarze = Lekarz.objects.all()
    return render(request, 'wyswietl_lekarza.html', {
        'lekarze': lekarze
    })


def export_leki(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Nazwa', 'Substancja czynna', 'Cena'])

    for lek in Lek.objects.all().values_list('nazwa', 'substancja_czynna', 'cena'):
        writer.writerow(lek)

    response['Content-Disposition'] = f'attachment; filename="leki_{datetime.date.today()}.csv"'

    return response


def export_lekarze(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Imie i Nazwisko', 'Numer telefonu', 'Email', 'Specjalizacja'])

    for lekarz in Lekarz.objects.all().values_list('imie_nazwisko', 'numer_telefonu', 'email', 'specjalizacja'):
        writer.writerow(lekarz)

    response['Content-Disposition'] = f'attachment; filename="lekarze_{datetime.date.today()}.csv"'

    return response


def export_pacjenci(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Imie i Nazwisko', 'Numer telefonu', 'Email', 'Plec', 'Data urodzenia', 'Pesel'])

    for pacjent in Pacjent.objects.all().values_list('imie_nazwisko', 'numer_telefonu', 'email', 'plec', 'data_urodzenia', 'pesel'):
        writer.writerow(pacjent)

    response['Content-Disposition'] = f'attachment; filename="pacjenci_{datetime.date.today()}.csv"'

    return response


def export_recepty(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Lek', 'Data', 'Pacjent', 'Lekarz', 'Zalecenie'])

    for recepta in Recepta.objects.all().values_list('lek', 'data', 'pacjent', 'lekarz', 'zalecenie'):
        writer.writerow(recepta)

    response['Content-Disposition'] = f'attachment; filename="recepty_{datetime.date.today()}.csv"'

    return response
