# Crea un programa llamado BuscaNumeros.py que le pida al usuario que escriba números. El
# programa los irá añadiendo uno tras otro a una lista hasta que el usuario escriba 0. Entonces, le pedirá
# que diga un número y le indicará en qué posiciones de la lista aparece ese número.

numeros = []

while True:
    numero = int(input("Ingrese un número (o 0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero)

numero_buscar = int(input("Ingrese un número para buscar en la lista: "))

posiciones = [i for i, num in enumerate(numeros) if num == numero_buscar]

if posiciones:
    print(f"El número {numero_buscar} aparece en las posiciones: {', '.join(map(str, posiciones))}")
else:
    print(f"El número {numero_buscar} no aparece en la lista.")