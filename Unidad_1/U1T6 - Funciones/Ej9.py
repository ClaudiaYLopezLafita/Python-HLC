# Encuentra el mayor elemento de una lista de enteros determinada

x = [4, 6, 8, 24, 12, 200]

def mayor_elementor(x):
    x.sort(reverse=True)
    print (x[0])

mayor_elementor(x)
