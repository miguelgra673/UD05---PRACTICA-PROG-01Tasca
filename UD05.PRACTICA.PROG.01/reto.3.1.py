# Realiza un programa que lea una cantidad de dinero (múltiplo de 5) y tras ello desglose el cambio en billetes de 500,200,100,50,20,10,5 intentando dar el mínimo número de billetes.
# El programa mostrará por la salida estándar el número mínimo de billetes.
# Solicitar la cantidad de dinero (múltiplo de 5)
cantidad = int(input("Ingrese la cantidad de dinero (múltiplo de 5): "))

if cantidad % 5 != 0:
    print("La cantidad ingresada no es un múltiplo de 5.")
else:
    billetes_500 = billetes_200 = billetes_100 = billetes_50 = billetes_20 = billetes_10 = billetes_5 = 0

    while cantidad > 0:
        if cantidad >= 500:
            billetes_500 += 1
            cantidad -= 500
        elif cantidad >= 200:
            billetes_200 += 1
            cantidad -= 200
        elif cantidad >= 100:
            billetes_100 += 1
            cantidad -= 100
        elif cantidad >= 50:
            billetes_50 += 1
            cantidad -= 50
        elif cantidad >= 20:
            billetes_20 += 1
            cantidad -= 20
        elif cantidad >= 10:
            billetes_10 += 1
            cantidad -= 10
        elif cantidad >= 5:
            billetes_5 += 1
            cantidad -= 5

    print(f"\nDesglose mínimo de billetes:")
    print(f"Billetes de 500: {billetes_500}")
    print(f"Billetes de 200: {billetes_200}")
    print(f"Billetes de 100: {billetes_100}")
    print(f"Billetes de 50: {billetes_50}")
    print(f"Billetes de 20: {billetes_20}")
    print(f"Billetes de 10: {billetes_10}")
    print(f"Billetes de 5: {billetes_5}")
