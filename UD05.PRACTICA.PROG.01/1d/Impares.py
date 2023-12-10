# Crea un programa llamado Impares.py que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número, separados por comas.
num = int(input("Inserte un numero entero positivo: "))
printNumeros = ""
for i in range (num):
    if i % 2 != 0 and i <= num - 2:
        printNumeros = printNumeros + str(i) + ", "
    elif i == num - 2:
        printNumeros = printNumeros + str(i)

print(f"{printNumeros}")