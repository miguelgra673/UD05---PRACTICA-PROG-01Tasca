# Realiza un programa que lea una secuencia de números enteros, uno por línea.
# El programa deberá mostrar como resultado el número más alto, seguido del número más bajo, separados por un espacio.
# El programa incluirá una primera línea X, 1<=X<=100, indicando cuantos números a leer (esa línea no se tendrá en cuenta). Tras ello se leerán X números en las próximas X líneas.
X = int(input("Ingrese la cantidad de números a leer (X): "))

numero_mas_alto = float('-inf')  
numero_mas_bajo = float('inf')   

for _ in range(X):
    numero = int(input("Ingrese un número entero: "))
    
    if numero > numero_mas_alto:
        numero_mas_alto = numero
    
    if numero < numero_mas_bajo:
        numero_mas_bajo = numero

print(f"Número más alto: {numero_mas_alto}")
print(f"Número más bajo: {numero_mas_bajo}")
