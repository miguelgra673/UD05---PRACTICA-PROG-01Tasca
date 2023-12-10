# Crea un programa llamado FicheroPersonas.py que lea información de personas (nombre y edad) de
# un fichero de texto, y muestre por pantalla los datos de la persona más joven y más vieja del fichero. El formato del fichero será como el siguiente, y se deberá almacenar en una lista antes de procesar la
# información.

nombre_fichero = "C:\\Users\\2dam\\Desktop\\SGE\\2d\\personas.txt"

with open(nombre_fichero, 'r') as archivo:
    lineas = archivo.readlines()

personas = []
for linea in lineas:
    partes = linea.strip().split(';')
    if len(partes) == 2:
        nombre = partes[0]
        edad = int(partes[1])
        personas.append((nombre, edad))

if not personas:
    print("El fichero está vacío o el formato es incorrecto.")
else:
    persona_joven = min(personas, key=lambda x: x[1])
    persona_mayor = max(personas, key=lambda x: x[1])

    print("Persona más joven:")
    print(f"Nombre: {persona_joven[0]}, Edad: {persona_joven[1]}")

    print("\nPersona más vieja:")
    print(f"Nombre: {persona_mayor[0]}, Edad: {persona_mayor[1]}")

