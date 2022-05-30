from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dodaj_lekarza/', views.dodaj_lekarza),
    path('dodaj_pacjenta/', views.dodaj_pacjenta),
    path('dodaj_recepte/', views.dodaj_recepte),
    path('dodaj_lek/', views.dodaj_lek),
    path('wyswietl_lek/', views.wyswietl_lek),
    path('wyswietl_recepte/', views.wyswietl_recepte),

]