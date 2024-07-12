import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://verdictmma.com/fighter/alex-poatan-pereira"

response = requests.get(url)
if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')

    resultado = soup.find_all("div", class_="flex-grow")

    data = []
    for dados in resultado:
        # Encontrar a div com a classe text-sm dentro do elemento atual
        data_evento_div = dados.find("div", class_="text-sm text-gray-500 leading-none")
        if data_evento_div:
            # Extrair o texto do elemento encontrado
            data_evento = data_evento_div.text.strip()
        else:
            data_evento = None  # Ou você pode usar um valor padrão como uma string vazia

        data.append({'Data_Evento': data_evento})

    print(data)
else:
    print("erro ao conectar no site")
