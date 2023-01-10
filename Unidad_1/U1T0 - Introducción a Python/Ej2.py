#Aplicar formato a las variables mediante el método string.format().

#Escriba un programa para usar el método string.format() para formatear 
# las siguientes tres variables según la salida esperada.

#Salida: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

totalMoney = 1000
quantity = 3
price = 450
cad1 = "Tengo {1} euros para comprar {0} tarjetas gráficas por {2:.2f} dólares."

print(cad1.format(quantity,totalMoney,price))