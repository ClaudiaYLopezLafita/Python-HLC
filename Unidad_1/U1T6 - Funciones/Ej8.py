# Genere una lista de Python de todos los números pares entre 4 y 30

def listar_pares():
    lista=[]
    for x in range(4, 31, 2):
        lista.append(x)
    return lista


print(listar_pares())