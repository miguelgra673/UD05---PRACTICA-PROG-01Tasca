# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos_de_15 = 0
acumulado_pares = 0

for _ in range(10):
    numero = int(input("Ingrese un valor entero: "))

    if numero < 0:
        negativos += 1

    elif numero > 0:
        positivos += 1

    if numero % 15 == 0:
        multiplos_de_15 += 1

    if numero % 2 == 0:
        acumulado_pares += numero

print(f"\nCantidad de valores negativos: {negativos}")
print(f"Cantidad de valores positivos: {positivos}")
print(f"Cantidad de múltiplos de 15: {multiplos_de_15}")
print(f"Valor acumulado de números pares: {acumulado_pares}")