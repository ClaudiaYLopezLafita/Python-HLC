# pip install requests
import requests

# Terminator 2: The judgment day
# r = requests.get('https://www.filmaffinity.com/es/film576352.html')
# Monty Python's Life of Brian
r = requests.get('https://www.filmaffinity.com/es/film612331.html')

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
t = r.text

# print(t)


def titulo_original(t):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = t.find(etiqueta_titulo)
    titulo = t[pos_etiqueta_titulo:]
    titulo = titulo[:titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    return titulo


print("Título original:" + titulo_original(t))
