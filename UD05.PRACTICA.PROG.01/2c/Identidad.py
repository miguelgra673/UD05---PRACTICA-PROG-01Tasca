# Crea un programa llamado Identidad.py que le pida al usuario un tamaño de tabla N y luego le
# deje rellenar los datos de N filas y N columnas de enteros. Al finalizar, le deberá decir si la tabla que ha
# rellenado se corresponde o no con una matriz identidad. Una matriz identidad es aquella que tiene unos
# en su diagonal principal y ceros en el resto. Por ejemplo (para un tamaño 3 x 3):

N = int(input("Ingrese el tamaño de la tabla (N): "))

tabla = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        tabla[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

es_identidad = all(tabla[i][j] == 1 if i == j else tabla[i][j] == 0 for i in range(N) for j in range(N))

if es_identidad:
    print("La tabla ingresada es una matriz identidad.")
else:
    print("La tabla ingresada NO es una matriz identidad.")
