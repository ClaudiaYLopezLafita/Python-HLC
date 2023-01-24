#Agregue el elemento 7000 después de 6000 en la siguiente lista

## TRABAJAMOS CON LISTAS ANIDADAS
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#accedemos a elemento en la posicion 2 y dentro de ese elemento accedemos 
#al elemento en posicion dis 
list1[2][2].append(7000)
print(list1)