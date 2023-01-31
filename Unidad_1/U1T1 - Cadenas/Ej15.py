
# Ejercicio 15
# Eliminar símbolos / puntuación especiales de una cadena determinada

##CONSEJO: uso de maketrans -- string.punctiation 
## traslate() -- intercambia ediante caracteres ascii
## str.translate(str.maketrans('','',string.punctuation))

str = input("Introduce una cadena: ")
strN =""

for x in str:
    if x.isalnum() or x==" ":
        strN = strN+x

print(strN)