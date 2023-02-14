## Escriba un programa para crear una función calcular() tal que pueda aceptar dos variables 
## y calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una única 
## llamada de retorno.

def calcula(n1, n2):
    sum = n1+n2
    rest = n1-n2
    print(f"Para los parámetros {n1} y {n2}, la suma es: {sum} y la resta es: {rest}")

calcula(int(input('N1: ')),int(input('N2: ')))