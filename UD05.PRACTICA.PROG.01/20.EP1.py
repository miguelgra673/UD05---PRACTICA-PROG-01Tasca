# Se tiene la siguiente lista:
# lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
# Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
# Volver a imprimir la lista.
lista_enteros = []
for i in range(5):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista_enteros.append(elemento)

lista_enteros.sort()
print("Lista ordenada de menor a mayor:", lista_enteros)

lista_enteros.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista_enteros)
