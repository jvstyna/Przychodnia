from django.db import models
from django.utils import timezone
# Create your models here.
SPECJALIZACJE = [('Internista', 'Internista'),
                ('Pediatra', 'Pediatra'),
                ('Ginekolog', 'Ginekolog'),
                ('Chirurg', 'Chirurg'),
                ('Ortopeda', 'Ortopeda'),
                ('Laryngolog', 'Laryngolog'),
                ('Okulista', 'Okulista'),
                ('Kardiolog', 'Kardiolog'),
                ('Urolog', 'Urolog'),
                ('Psychiatra', 'Psychiatra')]

PLEC = [('K', 'Kobieta'),
        ('M', 'Mężczyzna')]


class DaneOsobowe(models.Model):
    imie_nazwisko = models.CharField(max_length=50)
    numer_telefonu = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    class Meta:
        abstract = True


class Lekarz(DaneOsobowe):
    specjalizacja = models.CharField(max_length=30,
                                     choices=SPECJALIZACJE)

    def __str__(self):
        return self.imie_nazwisko


class Pacjent(DaneOsobowe):
    plec = models.CharField(max_length=1, choices=PLEC)
    data_urodzenia = models.DateField()
    pesel = models.IntegerField()

    def __str__(self):
        return self.imie_nazwisko


class Lek(models.Model):
    nazwa = models.CharField(max_length=100)
    substancja_czynna = models.CharField(max_length=100)
    cena = models.IntegerField()

    def __str__(self):
        return self.nazwa

class Recepta(models.Model):
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE)
    lek = models.ManyToManyField(Lek)
    data = models.DateTimeField(default=timezone.now)
    zalecenie = models.TextField()
