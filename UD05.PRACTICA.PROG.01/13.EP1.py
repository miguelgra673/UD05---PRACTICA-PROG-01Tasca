# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

oracion = input("Ingresa una oración: ")
espacios_blancos = 0

for caracter in oracion:
    if caracter == " ":
        espacios_blancos += 1

print("Cantidad de espacios en blanco ingresados:", espacios_blancos)
