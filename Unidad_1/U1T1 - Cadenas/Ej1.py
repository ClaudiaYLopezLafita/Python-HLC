# Ejercicio 1
# Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena 
# formada por los tres caracteres del medio de una cadena determinada

str = input("Introduce una cadena: ")
indice = int(len(str)/2)
if indice > 7:
    str_2 = str[indice-1:indice+2]
else:
    print("La cadena tiene que tener una longitud mayor de 7 caracteres")