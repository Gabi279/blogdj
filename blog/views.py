from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Entry, Author, Director


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["vistas"] = Entry.objects.filter(image = 'image').order_by('-created_date')[:3]
        return context
    

"""vistas entradas"""
class EntryListView(ListView):
    template_name = "entradas/entradas.html"
    context_object_name = 'entrada'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword',)
        list = Entry.objects.filter(title = palabra_clave) 
        return list

class EntryCreateView(CreateView):
    template_name = "entradas/new_entry.html"
    model = Entry
    fields = ('__all__')


class EntryUpdateView(UpdateView):
    template_name = "entradas/up_entrada.html"
    model = Entry
    fields = ('__all__')
    success_url = '/'

class EntryDeleteView(DeleteView):
    template_name = "entradas/del_entradas.html"
    model = Entry
    success_url = '/'

    
"""vistas autores"""
class AuthorListView(ListView):
    template_name = "autores/autores.html"
    paginate_by = 5
    ordering = 'name'
    model = Author

class AuthorCreateView(CreateView):
    template_name = "autores/new_author.html"
    model = Author
    fields = ('__all__')
    success_url = '/'

class AuthorUpdateView(UpdateView):
    template_name = "autores/up_autor.html"
    model = Author
    fields = ('__all__')
    success_url = '/'

class AuthorDeleteView(DeleteView):
    template_name = "autores/del_autor.html"
    model = Author
    success_url = '/'

"""vistas directores"""
class DirectorListView(ListView):
    template_name = "directores/directores.html"
    paginate_by = 5
    ordering = 'name'
    model = Director

class DirectorCreateView(CreateView):
    template_name = "directores/new_director.html"
    model = Director
    fields = ('__all__')

class DirectorUpdateView(UpdateView):
    template_name = "directores/up_director.html"
    model = Director
    fields = ('__all__')
    success_url = '/'

class DirectorDeleteView(DeleteView):
    template_name = "directores/del_director.html"
    model = Director
    success_url = '/'


    
    
    

