## Escriba un programa para crear una función mostrar_empleado() 
## utilizando las siguientes condiciones.

# Debe aceptar el nombre y el salario del empleado y mostrar ambos.
# Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.

def mostrar_empleado(name,salary):
    if salary == "":
        salary = 9000
    
    print(f"El empleado {name} con salario {salary}€.")

mostrar_empleado(input('Nombre: '), input('Salario: '))

