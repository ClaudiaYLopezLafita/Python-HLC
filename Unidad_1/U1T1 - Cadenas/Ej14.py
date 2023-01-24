
# Ejercicio 14
# Eliminar cadenas vacías de una lista de cadenas

str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]

for x in str_list:
    if x == "":
        str_list.remove(x)

print(str_list)