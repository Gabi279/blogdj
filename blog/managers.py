from django.db import models

class HomeManager(models.Manager):

    def entrada_portada(self):
        return self.filter()