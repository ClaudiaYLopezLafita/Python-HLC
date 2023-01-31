
# Escriba un programa para mostrar solo aquellos números de una lista que cumplan 
# las siguientes condiciones.   
    # El número debe ser divisible por cinco. 
    # Si el número es mayor que 150, omítalo y pasa al siguiente número. 
    # Si el número es mayor que 500, detén el bucle

numeros = [12, 75, 150, 180, 145, 525, 50]
resultado=[]
for x in numeros:
    if(x%5==0 and x<=150):
        resultado.append(x)
    elif(x>500):
        break

print(f"Los numeros resultantes son: ")
for x in resultado:
    print(x)