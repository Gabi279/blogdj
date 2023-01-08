from django.urls import path
from . import views

app_name = 'urls_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('entradas', views.EntryListView.as_view(), name='entradas'),
    path('ver_entradas/<slug>', views.EntryDetail.as_view(), name='ver-entradas'),
    path('autores', views.AuthorListView.as_view(), name='autores'),
    path('autores_pdf', views.AuthorListPDFView.as_view(), name='autores-pdf'),
    path('directores', views.DirectorListView.as_view(), name='directores'),

    #create
    path('nueva_entrada', views.EntryCreateView.as_view(), name='nuevo-entrada'),
    path('nuevo_autor', views.AuthorCreateView.as_view(), name='nuevo-autor'),
    path('nuevo_director', views.DirectorCreateView.as_view(), name='nuevo-director'),

   #update
    path('modificar_entrada/<pk>', views.EntryUpdateView.as_view(), name='modificar-entrada'),
    path('modificar_autor/<pk>', views.AuthorUpdateView.as_view(), name='modificar-autor'),
    path('modificar_director/<pk>', views.DirectorUpdateView.as_view(), name='modificar-director'),
    
   #delete
    path('eliminar_entrada/<pk>', views.EntryDeleteView.as_view(), name='eliminar-entrada'),
    path('eliminar_autor/<pk>', views.AuthorDeleteView.as_view(), name='eliminar-autor'),
    path('eliminar_director/<pk>', views.DirectorDeleteView.as_view(), name='eliminar-director'),
    
]
