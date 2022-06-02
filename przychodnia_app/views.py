import io
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import DodajLek, DodajLekarza, DodajRecepte, DodajPacjenta, IloscLeku
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
            return redirect('wyswietl_lek')

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
            return redirect('wyswietl_lekarza')

    return render(request, 'dodaj_lekarza.html', {
        'form': form
    })


def dodaj_recepte(request):
    if request.method == 'GET':
        form = DodajRecepte()
        ilosci = []
        for i in range(10):
            ilosci.append(IloscLeku(prefix=f'lek{i}'))
    if request.method == 'POST':
        form = DodajRecepte(request.POST)
        ilosci = []
        for i in range(10):
            if request.POST[f'lek{i}-lek']:
                ilosci.append(IloscLeku(request.POST, prefix=f'lek{i}'))
        if form.is_valid() and all(f.is_valid() for f in ilosci):
            recepta=form.save()
            for ilosc in ilosci:
                zmienna = ilosc.save(commit=False)
                zmienna.recepta = recepta
                zmienna.save()
            return redirect('wyswietl_recepte')

    return render(request, 'dodaj_recepte.html', {
        'form': form,
        'ilosci': ilosci
    })


def dodaj_pacjenta(request):
    if request.method == 'GET':
        form = DodajPacjenta()
    if request.method == 'POST':
        form = DodajPacjenta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wyswietl_pacjenta')

    return render(request, 'dodaj_pacjenta.html', {
        'form': form
    })


def usun_lek(request, id):
    lek = Lek.objects.get(id=id)
    lek.delete()
    return HttpResponseRedirect(reverse('wyswietl_lek'))


def usun_lekarza(request, id):
    lekarz = Lekarz.objects.get(id=id)
    lekarz.delete()
    return HttpResponseRedirect(reverse('wyswietl_lekarza'))


def usun_recepte(request, id):
    recepta = Recepta.objects.get(id=id)
    recepta.delete()
    return HttpResponseRedirect(reverse('wyswietl_recepte'))


def usun_pacjenta(request, id):
    pacjent = Pacjent.objects.get(id=id)
    pacjent.delete()
    return HttpResponseRedirect(reverse('wyswietl_pacjenta'))


def wyswietl_lek(request):
    filter_by = request.GET.get('filterBy') or ''
    phrase = request.GET.get('phrase') or ''

    if filter_by and phrase:
        query_args = {
            '{0}__{1}'.format(filter_by, 'exact' if phrase.isnumeric() else 'icontains'): phrase
        }

        leki = Lek.objects.filter(**query_args)
    else:
        leki = Lek.objects.all()

    p = Paginator(leki, 5)
    page = request.GET.get('page')
    leki_na_stronie = p.get_page(page)

    return render(request, 'wyswietl_lek.html', {
        'leki': leki,
        'leki_na_stronie': leki_na_stronie,
        'filter_by': filter_by,
        'phrase': phrase,
    })


def wyswietl_recepte(request):
    filter_by = request.GET.get('filterBy') or ''
    phrase = request.GET.get('phrase') or ''

    if filter_by and phrase:
        query_args = {
            '{0}__{1}'.format(filter_by, 'exact' if phrase.isnumeric() else 'icontains'): phrase
        }

        recepta = Recepta.objects.filter(**query_args)
    else:
        recepta = Recepta.objects.all()

    p = Paginator(recepta, 5)
    page = request.GET.get('page')
    recepty_na_stronie = p.get_page(page)
    recepty = Recepta.objects.all()

    return render(request, 'wyswietl_recepte.html', {
        'recepty': recepty,
        'recepty_na_stronie': recepty_na_stronie,
        'filter_by': filter_by,
        'phrase': phrase
    })


def wyswietl_pacjenta(request):
    filter_by = request.GET.get('filterBy') or ''
    phrase = request.GET.get('phrase') or ''

    if filter_by and phrase:
        query_args = {
            '{0}__{1}'.format(filter_by, 'exact' if phrase.isnumeric() else 'icontains'): phrase
        }

        pacjent = Pacjent.objects.filter(**query_args)
    else:
        pacjent = Pacjent.objects.all()

    p = Paginator(pacjent, 5)
    page = request.GET.get('page')
    pacjenci_na_stronie = p.get_page(page)
    pacjenci = Pacjent.objects.all()

    return render(request, 'wyswietl_pacjenta.html', {
        'pacjenci': pacjenci,
        'pacjenci_na_stronie': pacjenci_na_stronie,
        'filter_by': filter_by,
        'phrase': phrase
    })


def wyswietl_lekarza(request):
    filter_by = request.GET.get('filterBy') or ''
    phrase = request.GET.get('phrase') or ''

    if filter_by and phrase:
        query_args = {
            '{0}__{1}'.format(filter_by, 'exact' if phrase.isnumeric() else 'icontains'): phrase
        }

        lekarz = Lekarz.objects.filter(**query_args)
    else:
        lekarz = Lekarz.objects.all()

    p = Paginator(lekarz, 5)
    page = request.GET.get('page')
    lekarze_na_stronie = p.get_page(page)
    lekarze = Lekarz.objects.all()

    return render(request, 'wyswietl_lekarza.html', {
        'lekarze': lekarze,
        'lekarze_na_stronie': lekarze_na_stronie,
        'filter_by': filter_by,
        'phrase': phrase
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


def wykres_lekarze(request):
    return render(request, 'wykres_lekarze.html')


def api_wykres_lekarze(request):
    labels = ['Internista', 'Pediatra','Ginekolog','Chirurg', 'Ortopeda', 'Laryngolog',
              'Okulista', 'Kardiolog','Urolog', 'Urolog', 'Psychiatra']
    data = {}
    for label in labels:
        data[label] = Lekarz.objects.filter(specjalizacja=label).count()

    return JsonResponse(data)


def wykres_pacjenci(request):
    return render(request, 'wykres_pacjenci.html')


def api_wykres_pacjenci(request):
    labels = ['K', 'M']
    data = {}
    for label in labels:
        data[label] = Pacjent.objects.filter(plec=label).count()

    return JsonResponse(data)


def zalacz_plik_leki(request):
    template = 'zalacz_plik.html'
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):

        _, created = Lek.objects.update_or_create(
            nazwa=column[0],
            substancja_czynna=column[1],
            cena=column[2]
        )
        print(created)
    return render(request, template)
