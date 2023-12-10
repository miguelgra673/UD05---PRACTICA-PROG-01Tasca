# Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
# La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
# [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
lista_resultado = []

for i in range(1, 51):
    sublista = list(range(1, i + 1))
    lista_resultado.append(sublista)

for sublista in lista_resultado:
    print(sublista)
