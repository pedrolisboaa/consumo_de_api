from django.shortcuts import render
from .models import EstadosBrasileiros
from .util import buscardor_previsao_tempo, data, hora


# Create your views here.

def index(request):
    estados = EstadosBrasileiros.objects.all()

    if request.method == 'POST':
        estado_selecionado = request.POST.get('estados', None)
        if estado_selecionado != "null":
            busc_no_banco = EstadosBrasileiros.objects.filter(sigla=estado_selecionado).first()
            requisicao_da_api =  buscardor_previsao_tempo(busc_no_banco.latitude, busc_no_banco.longitude)
    

            conteudo = {
                'estados': EstadosBrasileiros.objects.all(),
                'dados_meteorologicos': requisicao_da_api,
                'data': data(),
                'hora': hora(),
            }

            return render(request, 'index.html', conteudo)
            
            
    conteudo = {
        'estados': EstadosBrasileiros.objects.all(),
    }

    return render(request, 'index.html', conteudo)
   

  
