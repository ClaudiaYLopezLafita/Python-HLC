# Una función se define con la palabra clave "def", el nombre de la función,
# los parámetros, y tras cerrar el paréntesis, ":", y a continuación, de manera
# identada el cuerpo de la función.
def suma_sin_parametros():
    num1 = 5
    num2 = 7
    print(num1 + num2)


def suma_con_parametros(num1, num2):
    print(num1 + num2)


# Con return devolvemos un valor concreto que queramos.
# Ojo, TODAS las funciones en Python devuelven un valor. Si no hay return,
# se devuelve "None"
def suma_con_return(num1, num2):
    return num1+num2


def devuelve_none():
    print("Lo siguiente es un None")


print(devuelve_none())
suma_sin_parametros()
suma_con_parametros(5, 9)
print(suma_con_return(6, 7))

# Pasamos los valores por referencia...salvo los tipos básicos

# También podemos pasar los valores por nombre. Referenciando los parámetros
suma_con_parametros(num2=7, num1=4)


# E igualmente podemos poner los valores por defecto de los parámetros
def suma_parametros_defecto(num1=0, num2=0):
    print(num1 + num2)


suma_parametros_defecto()


# La sentencia "pass" indica que no se hace nada.
# Sirve para dejar las funciones vacías para una implementación futura
def no_hace_nada():
    pass


# En Python podemos hacer cosas que no pueden hacer otros lenguajes de programación
# como por ejemplo que una función retorne más de un valor.
def devuelvo_tres_valores():
    return 1, 2, 3


uno, dos, tres = devuelvo_tres_valores()
print(uno)
print(dos)
print(tres)

# ¿Y si no pongo una de las variables para recoger lo que retorna?
# uno, dos = devuelvo_tres_valores()
# Da error!. ¿Y si no quiero tener que declarar una variable para
# recoger algo de una función porque no me interesa?. ¡Hay solución!
# LA BARRA BAJA. Por fin servirá para algo más que nombres de variables
# y Funciones

uno, _, tres = devuelvo_tres_valores()


# Finalmente, podemos pasar argumentos indeterminados a una función.
# Lo que hace básicamente *args es expandirse formando una tupla con los valores que contiene.
def suma_indeterminados(*args):
    print(args)
    suma = 0
    for num in args:
        suma += num
    return suma


print(suma_indeterminados(1, 2, 3, 4, 5))


# También podemos pasar argumentos indeterminados a una función pero por nombre.
# Lo que hace básicamente **kwargs es expandir un diccionario con los parámetros y sus valores.
def suma_indeterminados_nombre(**kwargs):
    print(kwargs)
    suma = 0
    for num in kwargs.values():
        suma += num
    return suma


print(suma_indeterminados_nombre(uno=1, dos=2, tres=3, cuatro=4, cinco=5))