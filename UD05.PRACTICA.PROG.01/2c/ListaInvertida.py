# Crea un programa llamado ListaInvertida.py que le pida al usuario que introduzca un conjunto
# de nombres separados por comas, y le muestre por pantalla la misma lista en orden inverso.

entrada_usuario = input("Ingrese un conjunto de nombres separados por comas: ")

nombres = entrada_usuario.split(',')

nombres = [nombre.strip() for nombre in nombres]

print("Lista en orden inverso:")
for nombre in reversed(nombres):
    print(nombre)
