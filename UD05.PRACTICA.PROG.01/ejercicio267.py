# Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto. Abrir luego el archivo creado con un editor de texto.
archivo = open("datos.txt","w") 
archivo.write("Primer línea.\n") 
archivo.write("Segunda línea.\n") 
archivo.write("Tercer línea.\n")  
archivo.close() 