import requests
import pandas as pd 
data = pd.read_excel('')

#Definimos un pandas series
lista_url = data['Final URL'].unique()
print(len(lista_url))
print(lista_url)

comp = {'url':[],
        'url_destino':[],
        'match':[]}
for url in lista_url: 
  url_destino = requests.get(url).url
  comp['url'].append(url)
  comp['url_destino'].append(url_destino)
  comp['match'].append(url==url_destino)

url_2 = 'https://hogar.mercadolibre.com.co/'
print(requests.get(url_2).url)


while True:
     try:
         print(requests.get(url_2).url)
         break
     except ValueError:
         print("url not working")


comparar = pd.DataFrame(comp)
corregir = comparar[comparar['match']==False]
corregir.head(10)