# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos.

sueldos_manana = []
sueldos_tarde = []

print("Ingresar sueldos para el turno de mañana:")
for i in range(4):
    sueldo = float(input(f"Ingrese sueldo para el empleado {i + 1}: "))
    sueldos_manana.append(sueldo)
print("\nIngresar sueldos para el turno de tarde:")
for i in range(4):
    sueldo = float(input(f"Ingrese sueldo para el empleado {i + 5}: "))
    sueldos_tarde.append(sueldo)
print("Lista de sueldos para el turno de mañana:", sueldos_manana)
print("Lista de sueldos para el turno de tarde:", sueldos_tarde)
