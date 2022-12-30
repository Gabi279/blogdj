from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

from .managers import AuthorSalaryManager, HomeManager



class Entry(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)
    resume = models.TextField('resume', null=True)
    text = models.TextField('text')
    image = models.ImageField(("Imagen"), upload_to='Entry', null=True)
    slug = models.SlugField(editable=False, max_length=100, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, 
            null=True,
            default=timezone.now)

    objects = HomeManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)

class Author(models.Model):

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    document = models.IntegerField('DNI')
    salary = models.IntegerField('Sueldo')
    date_birth = models.DateTimeField(
        'Fecha de nacimiento', 
        blank=True,
        null=True,
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.name + ' ' + self.last_name

    objects = AuthorSalaryManager()

class Director(models.Model):

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    age = models.IntegerField('Edad')


    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'
    
    def __str__(self):
        return self.name + ' ' + self.last_name
