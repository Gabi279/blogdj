from datetime import date

from django.db import models
from django.db.models import Count, Max, Min, Avg


class HomeManager(models.Manager):

    def entrada_portada(self):
        return self.filter()

class AuthorSalaryManager(models.Manager):

    """ -calcular la diferencia de sueldo entre la persona con el sueldo mas alto y el sueldo mas bajo 
		-calcular el sueldo anual de persona seleccionada
		-hacer un update del sueldo de una persona aumentandolo en un %10, %15, %20 según se seleccione
		-calcular la edad a partir de la fecha de nacimiento"""

    """contar cantidad de registros según algún filtro"""
    def contar_visitas(self):
        resultado = self.annotate(
            num_visitas=Count('id')
        )
        return resultado

    """obtener los datos de la persona con el sueldo mas alto"""
    def calcular_sueldo_max(self):
        resultado = self.aggregate(Max('salary'))
        return resultado

    """obtener los datos de la persona con el sueldo mas bajo"""
    def calcular_sueldo_min(self):
        resultado = self.aggregate(Min('salary'))
        return resultado

    """calcular sueldo promedio"""
    def calcular_sueldo_promedio(self):
        resultado = self.aggregate(Avg('salary'))
        return resultado

    