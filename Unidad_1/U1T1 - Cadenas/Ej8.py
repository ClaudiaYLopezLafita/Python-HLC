# Ejercicio 8
# Busque todas las apariciones de "que" en una cadena dada, 
# independientemente que esté o no en mayúsculas.

str = input("Instroduce una cadena: ")
cont = str.casefold().count("que")
print(f"El recuento de 'que' es: {cont}")

