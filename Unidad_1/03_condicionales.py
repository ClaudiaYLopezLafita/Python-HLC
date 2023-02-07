#sintaxis basica
nota = int(input("Introduce la nota del alumno:"))

if nota < 5:
    print('Suspenso.')
    if nota < 3:
        print('Vaya caca')
else:
    print('Aprobado como mínino')

#No hay switch en python -- uso de ELIF

edad = int(input("Introduce la edad:"))

if edad < 18:
    print('No pueedes pasar')
elif edad >= 18:
    print('Pasa hasta la seccion 1')
elif edad >= 20:
    print('Pasa hasta la seccion 1')

## concatenacion de operadores de comparacion

if 0 < edad < 100:
    print('Edad correcta')
else:
    print('Edad incorrecta')

#operador in para comprobar si un valor esta dentro de una tupla

print('Asignaturas optativas')
asig = input('Escribe:')
if asig in ('DAW','HLC'):
    print('Si te puedes matricular')
else:
    print('No te puedes matricular')
