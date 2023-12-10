# Escribe un programa que lea en una línea el número de horas trabajadas y en otra línea el precio por hora.
# Calcula el salario neto semanal de un trabajador en función del número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes reglas:
# Las primeras 35 horas se pagan a tarifa normal.
# Las horas que pasen de 35 se pagan a 1.5 veces la tarifa normal.
# Al sueldo bruto se le aplicarán las siguientes tasas de impuestos:
# Los primeros 500 euros son libres de impuestos.
# Los siguientes 400 tienen un 25% de impuestos.
# Los restantes un 45% de impuestos.
# Imprime por la salida estándar el salario calculado.
# Solicitar el número de horas trabajadas y el precio por hora al usuario
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))

if horas_trabajadas <= 35:
    sueldo_bruto = horas_trabajadas * precio_por_hora
else:
    sueldo_bruto = 35 * precio_por_hora + (horas_trabajadas - 35) * 1.5 * precio_por_hora

if sueldo_bruto <= 500:
    salario_neto = sueldo_bruto
elif sueldo_bruto <= 900:
    salario_neto = 500 + 0.75 * (sueldo_bruto - 500)
else:
    salario_neto = 500 + 300 + 0.55 * (sueldo_bruto - 900)

print("Salario neto semanal:", salario_neto)
