from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Entry, Author
from blog.forms import EntryForm


class HomeView(TemplateView):
    template_name = "index.html"

class AuthorListView(ListView):
    template_name = "blog/autores.html"
    paginate_by = 5
    ordering = 'name'
    model = Author


