from traceback import print_tb

import requests
from bs4 import BeautifulSoup
import json
import re

lik = 'www.adasdas.com'


respuesta = requests.get(lik)
respuesta_soup = BeautifulSoup(respuesta.content, 'html.parser')

product = []

product_titulo = respuesta_soup.find_all('div', class_="title")
product_precio = respuesta_soup.find_all('div', class_="price")
product_stock = respuesta_soup.find_all('div', class_="stock")
product_code = respuesta_soup.find_all('div', class_="code")
product_imagens = respuesta_soup.find_all(src =True)

print(product_imagens)

for i in range(len(product_titulo)):

    titulo = product_titulo[i].get_text(strip=True)
    precio = product_precio[i].get_text(strip=True)
    stock = product_stock[i].get_text(strip=True)
    code = product_code[i].get_text(strip=True)

    stock = int(re.search(r'\d+', stock).group())

    producto = {
        'puesto': i+1,
        'titulo': titulo,
        'precio': precio,
        'stock': stock,
        'code': code
    }

    product.append(producto)

print(product)

json_data = json.dumps(product)


with open("product.json", "w", encoding="utf-8") as archivo:
    json.dump(product, archivo, indent=2, ensure_ascii=False)




#elements = respuesta_soup.find_all('ul', class_ = 'products')
#get_text (strip= True) quita los espacios en blanco
#print(element)
#print(imagen)



