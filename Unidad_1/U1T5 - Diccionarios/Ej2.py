# Fusionar los siguientes dos diccionarios en uno

dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

# El update()método inserta los elementos especificados en el diccionario.
# Los elementos especificados pueden ser un diccionario o un objeto iterable con pares de valores clave.
dict1.update(dict2)

print(dict1)
