## Escriba un programa para crear una función func1() que acepte una longitud 
## variable de argumentos e imprima su valor.

def func1(*args):
    for x in range(len(args)):
        print(args[x])

func1(1, 2, 3, 4, 5)
func1(1, 2)

