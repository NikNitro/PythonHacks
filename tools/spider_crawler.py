# Recupera el HttpResponse de una URL
from urllib.request import urlopen 
# Para hacer peticiones POST
import requests 
# Recupera el HttpResponse en HTML
from bs4 import BeautifulSoup as bs 
# Para no entrar en ciclos
from collections import deque

url = 'http://aaa.com/'
host = 'aaa'

# Aquí guardaremos todas las URLs visitadas
visited_url = set()
# Aquí guardaremos todas las URLs que tengamos pendiente visitar
queue_url = deque([url])

while len(queue_url)>0:
    new_url = queue_url.pop()
    visited_url.add(new_url)
    try:
        # Recuperamos el HttpResponse de la URL
        html_code = urlopen(new_url) 
        # Convertimos dicho HttpResponse en un formato más manejable
        soap = bs(html_code, 'html.parser', from_encoding='iso-8859-1')
        # Obtenemos todas las etiquetas html ‘a’
        links = soap.find_all('a')

        for l in links:
            # Miramos que tenga una hiperreferencia, podría ser una imagen
            if 'href' in l.attrs:
                # Obtenemos el atributo, eliminando las anclas si las hubiera
                another_url = l.attrs['href'].split('#')[0]
            
            # Si no hemos pasado antes por ella, la añadimos a la cola, solo si es del mismo host.
            if another_url not in visited_url and another_url not in queue_url and host in another_url:
                queue_url.append(another_url)
    except Exception as e:
        print('Error al obtener la url', new_url, ':', e)

            
print(visited_url)
