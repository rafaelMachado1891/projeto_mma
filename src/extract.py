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

    lutador = get_text_or_none(soup,"h1", "text-gray-800 text-base md:text-xl font-bold font-sans")
    
    lutas = soup.find_all("div", class_="flex-grow")

    data = []
    for dados in lutas:
        # Usar a função auxiliar para encontrar e extrair o texto
        #lutador = get_text_or_none(lutador, "h1", "text-gray-800 text-base md:text-xl font-bold font-sans")
        data_evento = get_text_or_none(dados, "div", "text-sm text-gray-500 leading-none")
        evento = get_text_or_none(dados, "div", "text-sm font-medium font-sans text-gray-500 text-right leading-none")
        desafiante = get_text_or_none(dados, "div","mt-2 text-base font-medium text-gray-800 font-sans leading-none")
        resultado = get_text_or_none(dados, "span","text-sm font-bold text-green-500 font-sans leading-none")
        round = get_text_or_none(dados, "span", "text-sm text-gray-500 leading-none")

        data.append({"Lutador": lutador,"Data_Evento": data_evento, "Evento": evento, "Desafiante": desafiante,"resultado":resultado, "round": round})
# 
    
else:
    print("erro ao conectar no site")

df = pd.DataFrame(data=data)

print(df)

df.to_parquet('dados_df.parquet', index=False)