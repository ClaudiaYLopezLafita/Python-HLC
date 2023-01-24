# Dada una lista anidada, extiéndala agregando la sublista ["h", "i", "j"]
# de tal manera que se vea como la siguiente lista

lista = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublista = ["h", "i", "j"]

lista[2][1][2].extend(sublista)

print(lista)