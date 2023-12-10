# Realiza un programa que lea una secuencia de números enteros en una misma línea y muestre como resultado la línea en orden inverso.
# El programa incluirá una primera línea X, 1<=X<=100, indicando cuantos números a leer (esa línea no se tendrá en cuenta). Tras ello, en la siguiente línea se leerán X números separados por espacios y se mostrará finalmente en una sola línea el resultado.
X = int(input("Ingrese la cantidad de números a leer (X): "))

numeros = input("Ingrese la secuencia de números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]

print("\nSecuencia en orden inverso:", end=" ")
for numero in reversed(numeros):
    print(numero, end=" ")
