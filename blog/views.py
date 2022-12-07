from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Entry


class BlogView(TemplateView):
    template_name = "blog/entry.html"


# def entry(request):
#     return render(request, 'blog/entry.html', {})
