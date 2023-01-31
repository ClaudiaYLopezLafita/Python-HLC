
# Ejercicio 17
# Encuentra palabras con alfabetos y números

str = input("Introduce una cadena: ")
strN =[]

temp = str.split()
for item in temp:
    if any(chr.isalpha() for chr in item) and any(chr.isdigit() for chr in item):
        strN.append(item)

for i in strN:
    print(i)