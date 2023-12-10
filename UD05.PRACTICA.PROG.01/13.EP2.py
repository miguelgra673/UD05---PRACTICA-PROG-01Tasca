# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. 
# Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

oracion = input("Ingresa una oración: ")
oracion_minusculas = oracion.lower()  # Convierte toda la oración a minúsculas
cantidad_vocales = 0

for caracter in oracion_minusculas:
    if caracter in "aeiou":
        cantidad_vocales += 1

print("Cantidad de vocales en la oración:", cantidad_vocales)
