from django.contrib import admin
from .models import Author, Entry, Director

admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Director)


