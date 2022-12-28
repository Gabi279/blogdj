from django.db import models
from django.utils import timezone

from .managers import HomeManager



class Entry(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)
    text = models.TextField()
    image = models.ImageField(("Imagen"), upload_to='Entry', null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    objects = HomeManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    document = models.IntegerField('DNI')
    salary = models.IntegerField('Sueldo')
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.name + ' ' + self.last_name


class Director(models.Model):

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    age = models.IntegerField('Edad')


    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'
    
    def __str__(self):
        return self.name + ' ' + self.last_name
