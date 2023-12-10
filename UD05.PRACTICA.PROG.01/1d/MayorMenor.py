# Crea un programa llamado MayorMenor.py que le pida al usuario que introduzca una secuencia de N
# números positivos (primero el usuario deberá indicar cuántos números va a introducir). Al final del
# proceso, el programa deberá mostrar por pantalla el valor del número mayor y el menor introducidos
# por el usuario. Por ejemplo:

nVeces = int(input("Dime cuántos números vas a introducir: ")) 
print(f"Escribe {nVeces} números")
mayor = 0
menor = nVeces
for i in range(nVeces):
    numero = float(input(f"Ingrese el numero: "))
    mayor = max(mayor,numero)
    menor = min(menor,numero)

print(f"El mayor es {mayor}")
print(f"El menor es {menor}")