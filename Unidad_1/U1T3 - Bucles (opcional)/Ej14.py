#Invertir un número entero dado
num = 75869
num_inverso=0

while num >= 1:
    num_inverso=num_inverso*10+num%10
    num=num//10

print(num_inverso)