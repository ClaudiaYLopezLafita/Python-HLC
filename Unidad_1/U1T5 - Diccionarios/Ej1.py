# A continuación se muestran las dos listas, conviértalo en el diccionario

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]
## declaramos un diccionario vacio
diccionario={}
## hacemos un bucle para ir asignando la key con su valor
for x in range(3):
    diccionario[keys[x]]=values[x]

print(diccionario)
