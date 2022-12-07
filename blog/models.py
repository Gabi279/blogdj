from django.conf import settings
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Autor(models.Model):

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
    
    def get_name(self):
        return self.name