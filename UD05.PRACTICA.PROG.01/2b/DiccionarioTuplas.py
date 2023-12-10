usuarios = ()
for x in range(0,4):
    dni = input("Dime el DNI")
    calle = input("Dime el DNI")
    puerta = input("Dime el DNI")
    piso = input("Dime el DNI")
    usuarios[dni] = (dni,calle,puerta,piso)

dni = input("Dime el dni a buscar")
if dni in usuarios:
    print(f"Esl usuario vive en la calle {usuarios[dni][calle]}")
