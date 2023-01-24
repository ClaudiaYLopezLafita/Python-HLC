
# Ejercicio 17
# Encuentra palabras con alfabetos y números

str = input("Introduce una cadena: ")
strN =""

for x in str.split(" "):
    print(x)
    if x.isalpha() and x.isnumeric() or x==" ":
        print(x)
        strN = strN+x

print(strN)