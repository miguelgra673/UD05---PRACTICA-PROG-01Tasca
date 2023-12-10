# Crea un programa llamado Notas.py que le pida al usuario 3 notas, y calcule la nota final según estas
# reglas:
# Si ninguna nota es mayor que 4, la nota final es 0
# Si algunas notas son mayores que 4 (pero no todas), la nota final es 2
# Si todas las notas son mayores que 4, la nota final será el 30% de la primera más el 20% de la
# segunda más el 50% de la tercera
n1 = float(input("Primera nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Tercera nota: "))

if n1 <= 4 and n2 <= 4 and n3 <= 4:
    n_total = 0
elif n1 > 4 or n2 > 4 or n3 > 4:
    n_total = 2
else:
    n_total = 0.3 * n1 + 0.2 * n2 + 0.5 * n3

print(f"La nota final es: {n_total}")