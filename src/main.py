import requests
from bs4 import  BeautifulSoup
import pandas as pd

url = "https://verdictmma.com/fighter/alex-poatan-pereira"

response = requests.get(url)
if response.status_code == 200: 
 
 soup = BeautifulSoup(response.text, 'html.parser')

 resultado = soup.find_all("div", class_="relative w-full justify-center")
 print(resultado)
else:
  print("erro ao conectar no site")


