# Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.
lista_enteros = []
for i in range(5):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    lista_enteros.append(elemento)

lista_enteros.sort()
print("Lista ordenada de menor a mayor:", lista_enteros)

lista_enteros.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista_enteros)
