# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores
lista_enteros = []

for i in range(5):
    valor = int(input(f"Ingrese el entero {i + 1}: "))
    lista_enteros.append(valor)

nueva_lista = [valor for valor in lista_enteros if valor < 10]

print("Nueva lista con elementos menores a 10:")
print(nueva_lista)
