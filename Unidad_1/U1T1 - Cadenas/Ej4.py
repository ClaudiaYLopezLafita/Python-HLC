# Ejercicio 4
# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,
# organice los caracteres de tal manera que todas las letras minúsculas deben ir primero.

str = input("Inserte una cadena con mayúsculas y minusculas: ")

strLower=""
strUpper=""

for x in str:
    if x.islower():
        strLower+=x
    else:
        strUpper+=x

print(strLower+strUpper)
