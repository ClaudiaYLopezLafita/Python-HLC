# Son objetos de tipo String


# Para formatear una cadena, el método format es muy útil. Para usarlo, podemos insertar {} dentro
# de la cadena, y de esta manera, formatear el dato externo que tenemos.

edad = 49
cadena = "Mi edad es {} años"
print(cadena.format(edad))

# Se puede formatear con unos indicadores para que se imprima el valor de la manera que quieras
# Puedes consultarlos todos en: https://www.w3schools.com/python/ref_string_format.asp

cadena = "Mi edad es {:.2f} años"
print(cadena.format(edad))

# Y también se pueden imprimir varios valores
panoja = 250000
cadena = "Mi edad es {:.2f} años y manejo {} euros"
print(cadena.format(edad, panoja))

# Para esos múltiples valores, se puede especificar el índice dentro de las llaves {1}
# para ordernar correctamente todos los valores.
cantidad = 3
dinero = 1000
precio = 450.748
resultado = "Tengo {1} euros para comprar {0} tarjetas gráficas por {2:.2f} euros."
print(resultado.format(cantidad, dinero, precio))

# Y Puedes imprimir un valor concreto más de una vez
resultado = "Tengo {1} euros para comprar {1} tarjetas gráficas por {2:.2f} euros."
print(resultado.format(cantidad, dinero, precio))

# E incluso le podemos dar nombres a los índices. Por si no te gustan los numeritos.
# Más expresivo pero más para escribir

pedido = "Tengo un {marca}, es un {modelo}."
print(pedido.format(marca="Kia", modelo="Ceed"))

# Se puede compactar todo de esta manera, utilizando f en el print y poniendo las
# variables entre las llaves {}
cantidad_ = 3
dinero_ = 1000
precio_ = 450.748
print(f"Tengo {dinero_} euros para comprar {cantidad_} tarjetas gráficas por {precio_:.2f} euros.")

# Las cadenas son arrays del
soy_un_array = "Hola pajarito sin cola"
print(soy_un_array[2])

# Podemos recorrer una cadena con un bucle for
for x in "banana":
    print(x)

# Para comprobar si una cadena está dentro de otra se puede ser la palabra 'in'
texto = "Dale like si te ha gustado y subscríbete al canal!"
print("like" in texto)

# o en un if
if "like" in texto:
    print("Si está like")

# Importante!! Se concatena con el + también
a = "Grefusa"
b = "Churruca"
c = a + b
print(c)

#
# Funciones más usadas
#

# len() - Obtiene la longitud de la cadena
# upper() - Convierte todo a mayúsculas
# lower() - Convierte todo a minúsculas
# capitalize() - Convierte la primera a mayúsculas
# count(sub) - Cuenta las veces que aparece la subcadena 'sub' dentro de otra
# find(sub) - Devuelve el menor índice de la subcadena 'sub' que se está buscando
# isdigit() - Devuelve True si la cadena está formada exclusivamente por números (dígitos)
# isalum() - Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter
# isalpha() - Devuelve verdadero si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter.
# split() - Devuelve una lista de las palabras de la cadena, usando sep como delimitador de palabras
# strip() - Devuelve una copia de la cadena con el espacio inicial y final suprimido.
# replace(old, new) - Devuelve una copia de la cadena en la que se han sustituido todas las apariciones de old por new
# rfind(sub) - Devuelve el índice máximo de la cadena para el que se encuentra la subcadena sub, tal que sub está contenido en cadena

nombre = input("Introduce tu nombre: ")
print("Tu nombre es: ", nombre.upper())
print("Tu nombre es: ", nombre.lower())
print("Tu nombre es: ", nombre.capitalize())


edad = input("Introduce la edad: ")
print(edad.isdigit())


while edad.isdigit() == False:
    print("Introduce un valor numérico")
    edad = input("Introduce la edad: ")


if int(edad) < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")