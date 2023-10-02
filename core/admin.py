from django.contrib import admin
from .models import EstadosBrasileiros

# Register your models here.

@admin.register(EstadosBrasileiros)
class EstadosBrasileirosAdmin(admin.ModelAdmin): 
    list_display = ['sigla', 'nome_do_estado', 'latitude', 'longitude']