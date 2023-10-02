import requests
from datetime import datetime
from decouple import config

def buscardor_previsao_tempo(latitude, longitude):

    TOKEN = config('TOKEN')
    lat = latitude
    lon = longitude
    site = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}8&lon={lon}&appid={TOKEN}&units=metric&lang=pt_br'


    requisicao = requests.get(site)
    requisicao_dicionario = requisicao.json()


    nuvens = requisicao_dicionario['weather'][0]['description']
    temperatura = requisicao_dicionario['main']['temp']
    umidade = requisicao_dicionario['main']['humidity']

    return [nuvens, temperatura, umidade]


def data():
    return datetime.now().strftime("%d/%m/%Y")
    

def hora():
    return datetime.now().strftime('%H:%M')
    
  
    
