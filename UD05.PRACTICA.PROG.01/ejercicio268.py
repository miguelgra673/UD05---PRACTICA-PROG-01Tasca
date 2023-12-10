# Leer el contenido del archivo de texto 'datos.txt'.
archivo = open("datos.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()