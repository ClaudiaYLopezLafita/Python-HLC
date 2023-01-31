
# Ejercicio 14
# Eliminar cadenas vacías de una lista de cadenas
# Se puede puede usar filter para list(filter(None, lista))
str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]

for x in str_list:
    if x == "" or x== None:
        str_list.remove(x)

print(str_list)