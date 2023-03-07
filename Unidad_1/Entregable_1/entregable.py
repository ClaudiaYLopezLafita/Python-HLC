# pip install requests
import requests
import re
import json

# TORRENTE: EL BRAZO TONTO DE LA LEY
# req = requests.get('https://www.filmaffinity.com/es/film334167.html')
## TO LESLIE
req = requests.get('https://www.filmaffinity.com/es/film925993.html')
### IRATI
# req = requests.get('https://www.filmaffinity.com/es/film401654.html')
### THE SON
# req = requests.get('https://www.filmaffinity.com/es/film766331.html')
## AVATAR: EL SENTIDO DEL AGUA
# req = requests.get('https://www.filmaffinity.com/es/film899895.html')
# req = requests.get('')

## obtenemos el html y  lo metemos en un variable
html_text = req.text

## Declaración del diccionario y listas para la formacion del diccionario
diccionario = {}
values = []
keys = ["Título original",
"Año", "Duración",
"País", "Dirección",
"Guión", "Música",
"Fotografía", "Reparto",
"Productora", "Género",
"Sinopsis"]

####### OBTENCION DE LA INFORMACIÓN DESEADA
## Cada vez que se obtenga un valor

def titulo_original(html_text):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = html_text.find(etiqueta_titulo)
    titulo = html_text[pos_etiqueta_titulo:]
    titulo = titulo[:titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    titulo = titulo.split('<')[0]
    return titulo

v_titulo = titulo_original(html_text)
values.append(v_titulo)
# print(f"Título original: {titulo_original(html_text)}")

def anyo(html_text):
    etiqueta_anyo = "<dt>Año</dt>"
    pos_etiqueta_anyo = html_text.find(etiqueta_anyo)
    anyo = html_text[pos_etiqueta_anyo:]
    anyo = anyo[:anyo.find("</dd>")].splitlines()[1].lstrip().rstrip()
    anyo = re.findall(r'\d+', anyo)[0]
    return anyo

v_anyo =  anyo(html_text)
values.append(v_anyo)
# print(f"Año: {anyo(html_text)}")

def duracion(html_text):
    etiqueta_duracion = "<dt>Duración</dt>"
    pos_etiqueta_duracion = html_text.find(etiqueta_duracion)
    duracion = html_text[pos_etiqueta_duracion:]
    duracion = duracion[:duracion.find("</dd>")].splitlines()[1].lstrip().rstrip()
    duracion = duracion.split('>')[1]
    return duracion

v_duracion = duracion(html_text)
values.append(v_duracion)
# print(f"Duranción: {duracion(html_text)}")

def pais(html_text):
    etiqueta_pais = "<dt>País</dt>"
    pos_etiqueta_pais = html_text.find(etiqueta_pais)
    pais = html_text[pos_etiqueta_pais:]
    pais = pais[:pais.find("</dd>")].splitlines()[1].lstrip().rstrip()
    pais = pais.split(';')[1]
    return pais

v_Pais = pais(html_text)
values.append(v_Pais)
# print(f"País: {pais(html_text)}")

def direccion(html_text):
    etiqueta_direccion = "<dt>Dirección</dt>"
    pos_etiqueta_direccion = html_text.find(etiqueta_direccion)
    direccion = html_text[pos_etiqueta_direccion:]
    direccion = direccion[:direccion.find("</dd>")]
    direccion = direccion[:direccion.find("</span>")].splitlines()[2].lstrip().rstrip()
    direccion = direccion.split('>')
    dic = len(direccion)
    direccion = direccion[dic-1]
    return direccion

v_Direccion = direccion(html_text)
values.append(v_Direccion)
# print(f"Dirección: {direccion(html_text)}")

def guion(html_text):
    etiqueta_guion = "<dt>Guion</dt>"
    pos_etiqueta_guion = html_text.find(etiqueta_guion)
    guion = html_text[pos_etiqueta_guion:]
    guion = guion[:guion.find("</dd>")].splitlines()[1].lstrip().rstrip()
    guion = guion.split('>')
    #lista aux
    gui = []
    gui2=[]
    gui3=[]
    ##filtro 
    for elem in guion:
        if '</span' in elem:
            gui.append(elem)
    for elem in gui:
        if ',</span' not in elem:
            gui2.append(elem)
    for elem in gui2:
        if '. </span' not in elem:
            elem = elem[:-6]
            gui3.append(elem)
    guion = ', '.join(gui3)
    return guion

v_Guion = guion(html_text)
values.append(v_Guion)
# print(f"Guión: {guion(html_text)}")

def musica(html_text):
    etiqueta_musica = "<dt>Música</dt>"
    pos_etiqueta_musica = html_text.find(etiqueta_musica)
    musica = html_text[pos_etiqueta_musica:]
    musica = musica[:musica.find("</dd>")].splitlines()[1].lstrip().rstrip()
    musica = musica.split('>')
    ##lista auxiliar
    music = []
    music2 = []
    ##filtro
    for elem in musica:
        if '</span' in elem:
            music.append(elem)
    for elem in music:
        if ',</span' not in elem:
            elem = elem[:-6]
            music2.append(elem)
    musica = ', '.join(music2)
    return musica

v_Musica = musica(html_text)
values.append(v_Musica)
# print(f"Musica: {musica(html_text)}")

def foto(html_text):
    etiqueta_fotografia = "<dt>Fotografía</dt>"
    pos_etiqueta_fotografia = html_text.find(etiqueta_fotografia)
    fotografia = html_text[pos_etiqueta_fotografia:]
    fotografia = fotografia[:fotografia.find("</dd>")]
    fotografia = fotografia[:fotografia.find("</span>")].splitlines()[1].lstrip().rstrip()
    fotografia = fotografia.split('>')
    fot = len(fotografia)
    fotografia = fotografia[fot-1]
    return fotografia

v_Foto = foto(html_text)
values.append(v_Foto)
# print(f"Fotografía: {foto(html_text)}")

def reparto(html_text):
    etiqueta_reparto = "<dt>Reparto</dt>"
    pos_etiqueta_reparto = html_text.find(etiqueta_reparto)
    reparto = html_text[pos_etiqueta_reparto:]
    reparto = reparto[:reparto.find("</div>")]
    reparto = reparto.split('>')
    ##array auxiliares
    lista_rep = []
    lista_rep2 = []
    lista_rep3 = []
    ##primer filtro -- nos quedamos con elem con </span (donde suele ir los nombres)
    for elem in reparto:
        if '</span' in elem:
            lista_rep.append(elem)
    ##segundo filtro -- nos quedamos con los elemtos que no sean ,</span
    for elem in lista_rep:
        if ',</span' not in elem:
            lista_rep2.append(elem)
    ##tercer filtro -- eleminamos los ultomos </span de cada elemetoS
    for elem in lista_rep2[:32]:
        elem = elem[:-6]
        lista_rep3.append(elem)
    ## lo pasamos a cadena
    reparto = ', '.join(lista_rep3)
    return reparto

v_Reparto = reparto(html_text)
values.append(v_Reparto)
# print(f"Reparto: {reparto(html_text)}")

def productora(html_text):
    etiqueta_productora = "<dt>Compañías</dt>"
    pos_etiqueta_productora = html_text.find(etiqueta_productora)
    productora = html_text[pos_etiqueta_productora:]
    productora = productora[:productora.find("</dd>")].splitlines()[2].lstrip().rstrip()
    productora = productora.split('>')
    ##lista aux
    pro = []
    pro2 = []
    pro3 = []
    ##filtro
    for elem in productora:
        if '</span' in elem:
            pro.append(elem)
    ##filtro 2
    for elem in pro:
        if ',</span' not in elem:
            pro2.append(elem)
    for elem in pro2:
        if '. </span' not in elem:
            elem = elem[:-6]
            pro3.append(elem)
    productora = ', '.join(pro3)
    return productora

v_productora = productora(html_text)
values.append(v_productora)
# print(f"Productora: {productora(html_text)}")

def genero(html_text):
    etiqueta_genero ="<dt>Género</dt>"
    pos_etiqueta_genero = html_text.find(etiqueta_genero)
    genero = html_text[pos_etiqueta_genero:]
    genero = genero[:genero.find("</dd>")].splitlines()[2].lstrip().rstrip()
    genero = genero.split('>')
    ## lista auxiliar
    gen = []
    ## filtro
    for elem in genero:
        if '</a' in elem:
            elem = elem[:-3]
            gen.append(elem)
    genero = ', '.join(gen)
    return genero

v_genero = genero(html_text)
values.append(v_genero)
# print(f"Genero: {genero(html_text)}")

def sinopsis(html_text):
    etiqueta_sinopsis ="<dt>Sinopsis</dt>"
    pos_etiqueta_sinopsis = html_text.find(etiqueta_sinopsis)
    sinopsis = html_text[pos_etiqueta_sinopsis:]
    sinopsis = sinopsis[:sinopsis.find("</dd>")].splitlines()[1].lstrip().rstrip()
    sinopsis = sinopsis.split('>')[1]
    return sinopsis

v_sinopsis = sinopsis(html_text)
values.append(v_sinopsis)
# print(f"Sinopsis: {sinopsis(html_text)}")

### Construccion del diccionarios apartir de dos listas
for i in range(len(keys)):
    diccionario[keys[i]] = values[i]

# print(diccionario)

diccionario = json.dumps(diccionario, indent=4, ensure_ascii=False)
print(diccionario)
