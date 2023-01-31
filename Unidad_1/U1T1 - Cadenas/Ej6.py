# Ejercicio 6
# Dadas dos cadenas, s1 y s2, cree una cadena mixta usando las siguientes reglas

# Nota: Cree una tercera cadena hecha del primer carácter de s1, 
# luego el último carácter de s2, Siguiente, el segundo carácter de s1 y 
# el segundo último carácter de s2, y así sucesivamente. 
# Los caracteres sobrantes van al final del resultado.

s1 = "Abc"
s2 = "Xyz"

s2=s2[::-1] ## le damos la vuelta a s2
len_s1=len(s1)
len_s2=len(s2)
len_total = len_s1 if len_s1>len_s2 else len_s2

resultado=""
for i in range(len_total):
    if(i<len_s1):
        resultado=resultado+s1[i]
    if(i<len_s2):
        resultado=resultado+s2[i]

print(resultado)