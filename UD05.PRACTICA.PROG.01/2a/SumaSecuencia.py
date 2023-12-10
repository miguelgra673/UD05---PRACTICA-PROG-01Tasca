# Crea un programa llamado SumaSecuencia.py que le pida al usuario una secuencia de números
# separados por espacios y calcule la suma total de esos números.
secuencia = input("Secuencia de numeros: ")
partes = secuencia.split(" ")
cont = 0

for i in range (len(partes)):
    cont = cont + int(partes[i])

print(f"{cont}")