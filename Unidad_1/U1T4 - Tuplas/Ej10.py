# Compruebe si todos los elementos de la siguiente tupla son iguales

tupla = (45, 45, 45, 45)

count=0

for x in tupla:
    if (x == 45):
        count =count+1

if count == len(tupla):
    print("Todos los elemento de la tupla son iguales")
