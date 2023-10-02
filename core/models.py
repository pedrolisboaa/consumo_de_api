from django.db import models

# Create your models here.
class EstadosBrasileiros(models.Model):
    sigla = models.CharField(max_length=2)
    nome_do_estado = models.CharField(max_length=50)
    latitude = models.CharField(max_length=15,)
    longitude = models.CharField(max_length=15,)

    def __str__(self):
        return self.sigla