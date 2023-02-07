#Cree un nuevo diccionario extrayendo las siguientes claves de un diccionario a continuación

diccionario = {
    "nombre": "Pikolo",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
}

keys = list(diccionario.keys())
key_interes=[keys[0],keys[2]]

diccionario_final={}

for x in range(len(key_interes)):
    if(key_interes[x]=='nombre'):
        diccionario_final[key_interes[x]]='Kelly'
    else:
        diccionario_final[key_interes[x]]=8000

print(diccionario_final)
