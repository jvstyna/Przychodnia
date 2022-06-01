from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dodaj_lekarza/', views.dodaj_lekarza, name='dodaj_lekarza'),
    path('dodaj_pacjenta/', views.dodaj_pacjenta, name='dodaj_pacjenta'),
    path('dodaj_recepte/', views.dodaj_recepte, name='dodaj_recepte'),
    path('dodaj_lek/', views.dodaj_lek, name='dodaj_lek'),
    path('wyswietl_lek/', views.wyswietl_lek, name='wyswietl_lek'),
    path('wyswietl_recepte/', views.wyswietl_recepte, name='wyswietl_recepte'),
    path('wyswietl_pacjenta/', views.wyswietl_pacjenta, name='wyswietl_pacjenta'),
    path('wyswietl_lekarza/', views.wyswietl_lekarza, name='wyswietl_lekarza'),
    path('wyswietl_lekarza/usun/<int:id>', views.usun_lekarza, name='usun_lekarza'),
    path('wyswietl_recepte/usun/<int:id>', views.usun_recepte, name='usun_recepte'),
    path('wyswietl_pacjenta/usun/<int:id>', views.usun_pacjenta, name='usun_pacjenta'),
    path('wyswietl_lek/usun/<int:id>', views.usun_lek, name='usun_lek'),
    path('export_leki/', views.export_leki, name='export_leki'),
    path('export_lekarze/', views.export_lekarze, name='export_lekarze'),
    path('export_pacjenci/', views.export_pacjenci, name='export_pacjenci'),
    path('export_recepty/', views.export_recepty, name='export_recepty'),
    path('wykres_lekarze/', views.wykres_lekarze, name='wykres_lekarze'),
    path('api/wykres_lekarze/', views.api_wykres_lekarze, name='api_wykres_lekarze'),
    path('wykres_pacjenci/', views.wykres_pacjenci, name='wykres_pacjenci'),
    path('api/wykres_pacjenci/', views.api_wykres_pacjenci, name='api_wykres_pacjenci'),
]