# Crea un diccionario de datos para la lista de todos los empleados cuyas claves sean los empleados, 
#y los datos, los datos por defecto que se dan a continuación. Con el diccionario resultado, accede 
#a sus datos e imprímelos.

empleados = ['Rodogiro', 'Atacuerdo', 'Caminancio']
datos = {"puesto": 'Desarrollador Facebook', "salario": 12000}
diccionario = {}

for x in range(len(empleados)):
    diccionario[empleados[x]] = datos

print(diccionario)