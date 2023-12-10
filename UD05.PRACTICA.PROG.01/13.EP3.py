# Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.

clave = input("Ingresa una clave: ")
longitud_clave = len(clave)

if 10 <= longitud_clave <= 20:
    print("Clave válida. Longitud:", longitud_clave)
else:
    print("Error: La clave debe tener entre 10 y 20 caracteres.")
