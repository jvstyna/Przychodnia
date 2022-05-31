from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DodajLek, DodajLekarza, DodajRecepte, DodajPacjenta
from .models import Pacjent, Lekarz, Lek, Recepta


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