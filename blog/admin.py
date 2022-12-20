from django.contrib import admin
from .models import Author, Entry, Director

admin.site.register(Author)
admin.site.register(Director)

class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'director',
    )

    search_fields = (
        'author',
        'title',
        'director',
    )

    list_filter = (
        'title',
    )

admin.site.register(Entry, EntryAdmin)



