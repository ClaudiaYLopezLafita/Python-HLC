# Ejercicio 5
# Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada

str = input("Introduce una cadena: ")

lower=0
upper=0
chtr=0
num=0

for x in str:
    if x.isnumeric():
        num = num+1
    elif x.islower():
        lower = lower+1
    elif x.isupper():
        upper = upper+1
    else:
        chtr = chtr+1

print("Recuentos totales de caracteres, dígitos y símbolos: ")
print(f"Mayusculas: {upper}")
print(f"Minusculas: {lower}")
print(f"Caracteres especiales: {chtr}")
print(f"Números: {num}")


