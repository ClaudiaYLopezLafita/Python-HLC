# Concatenar dos listas por índice

lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]
result = []

for x in lista1:
    result.append(x+lista2[lista1.index(x)]+" ")

resultF = [''.join(result)]

print(resultF)