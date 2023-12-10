# Luego mientras la variable 'linea' sea distinta a un string vacío imprimimos el contenido de la variable 'linea' evitando que genere un salto de línea la función print mediante la asignación del parámetro end con el valor de '':
# También dentro de la estructura while leemos las siguientes líneas.
# Podemos recorrer el archivo leyendo línea a línea utilizando la estructura repetitiva for:

archivo = open("datos.txt","r")
for linea in archivo:
    print(linea, end='')
archivo.close()