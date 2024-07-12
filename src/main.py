import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_text_or_none(soup_element, tag, class_name):
    element = soup_element.find(tag, class_=class_name)
    return element.text.strip() if element else None

url = "https://verdictmma.com/fighter/alex-poatan-pereira"

response = requests.get(url)
if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')

    resultado = soup.find_all("div", class_="flex-grow")

    data = []
    for dados in resultado:
        # Usar a função auxiliar para encontrar e extrair o texto
        data_evento = get_text_or_none(dados, "div", "text-sm text-gray-500 leading-none")
        evento = get_text_or_none(dados, "div", "text-sm font-medium font-sans text-gray-500 text-right leading-none")

        data.append({'Data_Evento': data_evento, "Card": evento})

    print(data)
else:
    print("erro ao conectar no site")
