#Crea una función interna para calcular la suma de la siguiente manera

# Cree una función externa que acepte dos parámetros a y b
# Cree una función interna dentro de una función externa que calculará la suma de a y b
# Por último, una función externa agregará 5 y lo devolverá

def function_ext(a,b):

    def function_int(n1,n2):
        sum = n1+n2
        return sum
    
    return function_int(a,b)

def function_ext_sum_cinco():
    sum = function_ext(10,10) + 5
    print(sum) 

function_ext_sum_cinco()


