# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

edades_manana = []
edades_tarde = []
edades_noche = []

for i in range(5):
    edades_manana.append(int(input(f"Ingrese la edad del estudiante {i + 1} del turno mañana: ")))

for i in range(6):
    edades_tarde.append(int(input(f"Ingrese la edad del estudiante {i + 1} del turno tarde: ")))

for i in range(11):
    edades_noche.append(int(input(f"Ingrese la edad del estudiante {i + 1} del turno noche: ")))

promedio_manana = sum(edades_manana) / len(edades_manana) if edades_manana else 0
promedio_tarde = sum(edades_tarde) / len(edades_tarde) if edades_tarde else 0
promedio_noche = sum(edades_noche) / len(edades_noche) if edades_noche else 0

print(f"\nPromedio de edades del turno mañana: {promedio_manana:.2f}")
print(f"Promedio de edades del turno tarde: {promedio_tarde:.2f}")
print(f"Promedio de edades del turno noche: {promedio_noche:.2f}")

turno_mayor_promedio = max([(promedio_manana, 'mañana'), (promedio_tarde, 'tarde'), (promedio_noche, 'noche')])

print(f"\nEl turno con el mayor promedio de edades es el turno {turno_mayor_promedio[1]} con un promedio de {turno_mayor_promedio[0]:.2f}.")
