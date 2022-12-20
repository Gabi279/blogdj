from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='entradas'),
    path('autores', views.AuthorListView.as_view(), name='autores'),
]
