# Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code.archi1=open("datos.txt","w", encoding="utf-8") 
archivo=open("datos.txt","w", encoding="utf-8")
archivo.write("Primer línea.\n") 
archivo.write("Segunda línea.\n") 
archivo.write("Tercer línea.\n")  
archivo.close() 