# Crea un programa llamado CuentaTexto.py que le pida al usuario un texto, y luego le diga
# cuántas veces aparece la palabra Python en ese texto
texto = str(input("Escriba un texto que contenga Python: "))
cont = 0

while texto.find("Python") >= 0:
    cont += 1
    texto = texto[(texto.find('Python') + 6):]    
    
print("Python aparece " + str(cont) + " veces")      