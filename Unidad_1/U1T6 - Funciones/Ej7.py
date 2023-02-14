## A continuación se muestra la función mostrar_estudiante(nombre, edad). 
## Asígnele un nuevo nombre muestra_alumno(nombre, edad) y llámelo usando el nuevo nombre.

def mostrar_estudiante(nombre, edad):
    print(nombre, edad)


def muestra_alumno(nombre, edad):
    print(mostrar_estudiante(nombre, edad))

mostrar_estudiante("Alumne", 26)
