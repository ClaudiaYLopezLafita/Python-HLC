# Ejercicio 18
# Reemplace cada puntuación con # en la siguiente cadena

str = input("Introduce una cadena: ")
strN =""

for x in str:
    if x.isalnum()==False or x==" ":
        strN = strN+x

print(strN)

