# Crea un programa llamado Factura.py que le pida al usuario precios para una factura, hasta que
# escriba 0. Entonces, el programa debe mostrar el total de la factura con 2 dígitos decimales.

entrada = int(input("Precios: "))
total = 0
while entrada != 0:
    total = total + entrada
    entrada = int(input("Precios: "))

print(f"Total de factura: {total}")