# Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido.
archivo = open("datos.txt","r")
lineas = archivo.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
archivo.close()