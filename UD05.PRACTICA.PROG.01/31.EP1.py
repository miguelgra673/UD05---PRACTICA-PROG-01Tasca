# Confeccionar un programa con las siguientes funciones:
# 1)Cargar una lista de 5 enteros.
# 2)Retornar el mayor y menor valor de la lista mediante una tupla.
# Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargar_lista():
    lista = []
    for i in range(5):
        valor = int(input(f"Ingrese el entero {i + 1}: "))
        lista.append(valor)
    return lista

def obtener_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

mi_lista = cargar_lista()

mayor, menor = obtener_mayor_menor(mi_lista)

print("Mayor valor:", mayor)
print("Menor valor:", menor)
